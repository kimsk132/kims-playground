"""
Author: Pairode Jaroensri
Last revision: Feb 28

This program plots the CPU temperature in real time with poll rate of 1 Hz.
Dependencies: lm-sensors, numpy, matplotlib
Before using it, please change the ANIMATE function to match your system's lm-sensors output.
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib import animation

fig, ax = plt.subplots()
ax.yaxis.tick_right()
ax.yaxis.set_label_position("right")
ax.set_ylim([0, 100])
ax.set_xlim([-60, 0])
ax.set_xlabel("Time (s)")
ax.set_ylabel("CPU Temp (°C)")
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(2))
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(2))

for i in range(0, 10):
    plt.axhline(i*10, color='0.75')



x = np.arange(-59, 1, 1)
temps = []
for i in range(60):
    temps.append(0)

line, = ax.plot(x, temps)
line.set_color('r')

def animate(i):
    global temps
    sensors = os.popen('sensors').read()
    physical = float(sensors[349:353]) # Change the string slicing to match your system output
    # core0 = float(sensors[409:413])
    # core1 = float(sensors[469:473])
    print(physical, "°C")
    temps.append(physical)
    temps.pop(0)
    line.set_ydata(temps)  # update the data
    return line,


# Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.zeros(60))
    return line,

ani = animation.FuncAnimation(fig, animate, [0], init_func=init,
                              interval=1000, blit=True)
plt.show()
