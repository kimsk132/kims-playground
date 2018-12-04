"""
Animate an orbit of a planet around a star.
Change line 69 to enable shading to demonstrate Kepler Law of Area.
Author: Pairode Jaroensri
Last visited: May 6, 2017
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

AU=(149.6e6 *1000)
G = 6.67428e-11

class body: 
    def __init__(self, x_pos=0, y_pos=0, x_vel=0, y_vel=0, mass=0, sym='o'):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.mass = mass
        self.net_force = []
        self.symbol = sym
        
    # returns a list of [force_x, force_y]
    def calc_force(self, other):
        r_square = (other.x_pos - self.x_pos) ** 2 + (other.y_pos - self.y_pos) ** 2
        force = G * self.mass * other.mass / r_square
        force_x = force * (other.x_pos - self.x_pos) / np.sqrt(r_square)
        force_y = force * (other.y_pos - self.y_pos) / np.sqrt(r_square)
        return [force_x, force_y]
    
    def calc_net_force(self, all_bodies):
        net_force_x = 0
        net_force_y = 0
        for a_body in all_bodies:
            if (not(a_body is self)):
                force = self.calc_force(a_body)
                net_force_x += force[0]
                net_force_y += force[1]
        return [net_force_x, net_force_y]
    
    def update(self, dt, force_x, force_y):
        self.x_vel += force_x * dt / self.mass
        self.y_vel += force_y * dt / self.mass
        self.x_pos += self.x_vel * dt
        self.y_pos += self.y_vel * dt
        
    def draw(self):
        plt.plot(self.x_pos, self.y_pos, self.symbol)
        

sun = body(0, 0, 0, 0, 1.99e30, 'o')
planet_x = body(AU, 0, 0, 1e4, 6e24, 'o')
bodies = [sun, planet_x]
dt = 24*360

fig = plt.figure()
ax = plt.axes(xlim=(-.5e11, 1.8e11), ylim=(-.5e11, .5e11))
line, = ax.plot([], [], lw=2)
line2, = ax.plot([], [], lw=2)
shader, = ax.plot([], [], lw=2)
# From Stack Overflow
history_x = []
history_y = []
shader_x = []
shader_y = []
counter = 0
enable_shading = True # change to True to enable shading
shade = enable_shading

def init():
    line.set_data([], [])
    line2.set_data([], [])
    shader.set_data([], [])
    return line,

def animate(i):
    global sun, planet_x, bodies, dt, history_x, history_y, counter, shade, shader_x, shader_y, enable_shading
    counter = (counter + 1) % 300
    if enable_shading and counter == 0:
        shade = not shade
    lst_fx = {}
    lst_fy = {}
    for a_body in bodies:
        force = a_body.calc_net_force(bodies)
        lst_fx[a_body] = force[0]
        lst_fy[a_body] = force[1]
    for a_body in bodies:
        a_body.update(dt, lst_fx[a_body], lst_fy[a_body])
    history_x.append(planet_x.x_pos)
    history_y.append(planet_x.y_pos)

    line.set_data(history_x, history_y)
    line2.set_data([b.x_pos for b in bodies], [b.y_pos for b in bodies])
    xx = np.linspace(sun.x_pos, planet_x.x_pos, 100)
    yy = np.linspace(sun.y_pos, planet_x.y_pos, 100)
    if shade:
        shader_x.extend(xx)
        shader_y.extend(yy)
    shader.set_data(shader_x, shader_y)

    return line, line2, shader

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=1, blit=True)
plt.show()