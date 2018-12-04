"""
Python3 script for reading in and plotting diode data from the Physics 111A lab curve tracer.
This script assume that the first line in the file is the column labels, which we will discard.
Dependency: matplotlib.pyplot for plotting.
Author: Pairode Jaroensri
Last visited: June 19, 2017
"""
import matplotlib.pyplot as plt

def read_file(filename, x_list, y_list):
    # Open the file
    scr = open(filename, "r")

    # Skipping the first line in the file, which I assume to be the labels, not data.
    lines_iter = iter(scr)
    next(lines_iter)

    # Reading from the file and filling the lists
    for line in lines_iter:
        vals = line.split()
        x_list.append(vals[0])
        y_list.append(vals[1])

    # Close the file
    scr.close()

# Creating lists for plotting
d_voltage = []
d_current = []

read_file("Diode_room_temp.dat", d_voltage, d_current)

r_voltage = [0.085, 0.250, 0.52, 3.43, 7.40]
r_current = [0.00000882979276, 0.0000259699787, 0.00005360203605, 0.0003564119877, 0.0007681919701]


# Finally plot the lists.
plt.plot(d_voltage, d_current)
# plt.plot(r_voltage, r_current)
plt.xlabel("Voltage (V)")
plt.ylabel("Current (A)")
plt.show()
