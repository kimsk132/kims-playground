"""
Author: Pairode Jaroensri
Last revision: Feb 28, 2018

This program plots the CPU temperature in real time with the poll rate of 1 Hz.
Dependencies: lm-sensors, numpy, matplotlib
Before using it, please change the ANIMATE function to match your system's lm-sensors output.
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib import animation

# Set up the figure
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

# Define history range and temperature polling interval
x = np.arange(-60, 1, 1)
temps = []
for i in range(61):
    temps.append(None)

line, = ax.plot(x, temps)
line.set_color('r')

def animate(i):
    global temps
    sensors = os.popen('sensors').read()
    physical = float(sensors[349:353])
    # Change the string slicing of the above line to match your system output
    # The slicing should give you the desired sensor reading from lm-sensors
    print(physical, "°C")
    temps.append(physical)
    temps.pop(0)
    line.set_ydata(temps)  # update the data
    return line,

def init():
    line.set_ydata(np.zeros(60))
    return line,

ani = animation.FuncAnimation(fig, animate, [0], init_func=init,
                              interval=1000, blit=True)
plt.show()
