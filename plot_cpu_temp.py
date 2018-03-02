"""
Author: Pairode Jaroensri
Last revision: March 1, 2018

This program plots the CPU temperature in real time with the poll rate of FREQUENCY Hz
and plotting up to TIME_LENGTH seconds back.
FREQUENCY is best kept under 5 Hz.
Dependencies: lm-sensors, matplotlib

Remark:
Before using it, you might need to change the variable PAT in GET_CPU_TEMP function
to match your system's lm-sensors output.
"""

import os, re
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib import animation
from collections import deque

frequency = 2
time_length = 60

def get_cpu_temp():
    sensors = os.popen('sensors').read()
    pat = 'Physical id 0:\s*(\+?\d+\.?\d?)°C'
    m = re.search(pat, sensors)
    return float(m.group(1))

def animate(temps):
    physical = get_cpu_temp()
    print(physical, "°C")
    temps.append(physical)
    temps.popleft()
    line.set_ydata(temps)  # update the data
    return line,

def init():
    line.set_ydata([None for i in range(-time_length*frequency,1)])
    return line,

if __name__ == '__main__':
    # Set up the figure
    fig, ax = plt.subplots()
    plt.title("CPU temperature")
    ax.yaxis.tick_right()
    ax.yaxis.set_label_position("right")
    ax.set_ylim([0, 100])
    ax.set_xlim([-time_length, 0])
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("CPU Temp (°C)")
    ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(2))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(2))
    for i in range(0, 10):
        plt.axhline(i*10, color='0.75')

    # Define history range and temperature polling interval
    x = [i/frequency for i in range(-time_length*frequency,1)]
    temps = deque()
    for i in range(time_length*frequency+1):
        temps.append(None)
    assert len(x) == len(temps)

    line, = ax.plot(x, temps)
    line.set_color('r')

    ani = animation.FuncAnimation(fig, animate, [temps], init_func=init,
                                  interval=1000/frequency, blit=True)
    plt.show()
