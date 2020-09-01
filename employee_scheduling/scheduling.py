import cvxpy as cp
import numpy as np
import pandas as pd

# Read in the preference table.
preference_table = pd.read_csv('./employee_preferences.csv', index_col=0)
# n = num employees
# m = number of shifts
n, m = preference_table.shape
# Read in the shift requirements
shift_requirements = pd.read_csv('./shift_requirements.csv', index_col=0)
shift_numpy = shift_requirements.to_numpy()
shift_people = shift_numpy[0]
shift_hours = shift_numpy[1]
# Read in employee requirements
employee_requirements = pd.read_csv('./employee_requirements.csv', index_col=0)
employee_hours = employee_requirements.to_numpy().reshape(n)

# Deciding the "infeasibility" threshold.
# The cost should be lower than threshold if every employee can work the shift they are assigned to.
dislike_factor = preference_table.max().max()
threshold = n * dislike_factor * 100

# Fill the blanks in preference_table with this threshold
preference_table = preference_table.fillna(threshold)

# Define the optimization problem
X = cp.Variable((n, m), boolean=True)
C = cp.Parameter((n, m))
C.value = preference_table.to_numpy()

# Add constrains here or comment out the ones you dont need
constraints = [
	# X @ shift_hours >= employee_hours, 	# Each employee must take a certain number of hours as defined in employee_requirements
	np.ones(n) @ X >= shift_people 	# Each shift needs a certain number of employees as defined in shift_requirements
]

# Handling overlapping shifts
with open('overlap.csv') as f:
    f.readline()
    for line in f:
        current_line = line.rstrip().split(',')
        print(current_line)
        shift_indices = [preference_table.columns.get_loc(shift) for shift in current_line if shift]
        constr = 0
        for shift in shift_indices:
            constr += X[:,shift]
        constraints.append(constr <= 1)

# First term reflects the employee's preferences, and the second term is trying to minimizes the number of hours each person works
obj = cp.Minimize(cp.sum(cp.multiply(C, X) @ shift_hours) + cp.sum_squares(cp.pos(X @ shift_hours - employee_hours) * dislike_factor * 2))

prob = cp.Problem(obj, constraints)
prob.solve(verbose=True)

assignment = pd.DataFrame(X.value,
					index = preference_table.index,
					columns = preference_table.columns).round()

print("Status: ", prob.status)
print("The optimal cost is", prob.value)
print("A solution is")
print(assignment)
if prob.value >= threshold:
	print("WARNING: Some employees are scheduled to work the shift they cannot make. Time to hire more people?")

assignment.to_csv('./assignment.csv')
