import numpy as np
import pandas as pd
import cvxpy as cp
import json

# Read in form responses
responses = pd.read_csv('form_responses.csv', index_col=2)
responses.drop('Timestamp', axis=1, inplace=True)
responses.drop('Email Address', axis=1, inplace=True)
responses.drop('Privacy Policy', axis=1, inplace=True)
responses.drop('Instruction', axis=1, inplace=True)

# Read in how many hours per week each person needs to work
employee_hours = responses['Hours per week'].to_numpy()

# Generate preference_table
preference_table = responses.copy()
preference_table.drop('Hours per week', axis=1, inplace=True)
# n = num employees
# m = number of shifts
n, m = preference_table.shape

# Replace preference words with weight value we defined in "preference_scheme.json"
with open("preference_scheme.json") as f:
    preference_scheme = json.load(f)

for pref, weight in preference_scheme.items():
    preference_table.replace(pref, weight, inplace=True)

# Deciding the "infeasibility" threshold.
# The cost should be lower than threshold if every employee can work the shift they are assigned to.
dislike_factor = preference_table.max().max()
threshold = n * dislike_factor * 100

# Fill the blanks in preference_table with this threshold
preference_table.fillna(threshold, inplace=True)

# TODO: Read in shift requirements
shift_requirements = pd.read_csv('./shift_requirements.csv', index_col=0)
shift_numpy = shift_requirements.to_numpy()
shift_people = shift_numpy[0]
shift_hours = shift_numpy[1]

# Make sure the shift requirement is consistent with preference table
assert all(shift_requirements.columns == preference_table.columns), "Shift requirement table must have the same columns as preference table."

# Define the optimization problem
X = cp.Variable((n, m), boolean=True)
C = cp.Parameter((n, m))
C.value = preference_table.to_numpy()

# Add constrains here.
constraints = [
    X @ shift_hours >= employee_hours,    # Each employee must take a certain number of hours as defined in employee_requirements
    np.ones(n) @ X >= shift_people  # Each shift needs a certain number of employees as defined in shift_requirements
]

# Handling overlapping shifts
with open('overlap.csv') as f:
    f.readline()
    for line in f:
        current_line = line.rstrip().split(',')
        shift_indices = [preference_table.columns.get_loc(shift) for shift in current_line if shift]
        constr = 0
        for shift in shift_indices:
            constr += X[:,shift]
        constraints.append(constr <= 1)

# First term reflects the employee's preferences, and the second term is trying to minimizes the number of hours each person works
obj = cp.Minimize(cp.sum(cp.multiply(C, X) @ shift_hours) + cp.sum_squares(cp.pos(X @ shift_hours - employee_hours) * dislike_factor * 2))

prob = cp.Problem(obj, constraints)
prob.solve(solver="SCIP", scip_params={'limits/gap':0}, verbose=True) # Adjust gap tolerance here

assignment = pd.DataFrame(X.value,
                    index = preference_table.index,
                    columns = preference_table.columns).round().astype('int')

print("Status: ", prob.status)
print("The optimal cost is", prob.value)
print("A solution is")
print(assignment)
assignment.to_csv('./raw_output.csv')

# Format the output to be easy to read
output = {}
for name, row in assignment.iterrows():
    assigned = []
    for shift, value in row.iteritems():
        if value == 1:
            assigned.append(shift)
    output[name] = assigned

with open('assignment.json', 'w') as f:
    json.dump(output, f, sort_keys=True, indent=4)

# Check that everyone can make the shifts they are assigned
assignment_cost = C.value * X.value
if (assignment_cost >= threshold).any():
    print("WARNING: Some people are scheduled to work the shift they cannot make.")
    for row_idx, row in enumerate(assignment_cost):
        for col_idx, cost in enumerate(row):
            if cost >= threshold:
                print("{} cannot make {}".format(assignment.index[row_idx], assignment.columns[col_idx]))

# Check if anyone is assigned more hours than they need to work
number_hours = X.value @ shift_hours
if (number_hours >= employee_hours).any():
    print("WARNING: Some people are assigned more hours than they need.")
    for name_idx, hours in enumerate(number_hours):
        if hours > employee_hours[name_idx]:
                print("{} is assigned {} hours, but needs {}".format(assignment.index[name_idx], number_hours[name_idx], employee_hours[name_idx]))

print("\nResult is saved as 'assignment.json' and 'raw_output.csv'")
