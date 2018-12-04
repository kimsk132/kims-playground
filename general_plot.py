import numpy as np
import matplotlib.pyplot as plt
import math as m

# Define your function here:
f = lambda x: 5*x*m.exp(-2*x)

# Define your xmin, xmax, interval here
xmin = 0
xmax = 5
num_sample = 100
x = np.linspace(xmin, xmax, num_sample)
y = np.zeros(num_sample)
for i in range(num_sample):
    y[i] = f(x[i])

# Finally plot the lists.
plt.plot(x, y)

# plt.xlabel("")
# plt.ylabel("")
plt.show()
