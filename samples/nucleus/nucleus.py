# This program simulate motion of electron around the nucleus of an atom using
# Classical Physics and Coulomb's Law. The nucleus is assumed to be stationary.
# source: www.techforcurious.website
# http://techforcurious.website/simulation-of-motion-of-electron-around-nucleus-of-an-atom-vpython-tutorial-6-visual-python/

from vpython import *

# Defining Display

scene2 = canvas(width=800, height=500, background=vector(1, 1, 1))

# Defining Constants

pi = 2 * asin(1.0)  # Defining value of pi using sin(pi/2) = 1
a0 = 0.529177e-10  # Radius of first orbit
m_p = 1.6726219e-27  # Mass of Proton
m_e = 9.10938356e-31  # Mass of Electron
e = 1.6021765e-19  # Charge of Electron
epsilon = 8.854187e-12  # Permittivity of free space
v_e = e / sqrt(
    4 * pi * epsilon * a0 * m_e)  # Using Classical Physics: mv^2/r = e^2/(4*pi*epsilon*r^2)
print("Radius of First Orbit = ", a0)
print("Velocity of Electron in First Orbit = ", v_e)

# Defining 3D Objects

nucleus = sphere(pos=vector(0, 0, 0), radius=0.1 * a0, velocity=vector(0, 0, 0), mass=m_p, charge=e,
                 color=color.yellow)
# electron = sphere(pos=vector(a0, 0, 0), radius=0.02 * a0, velocity=vector(0, v_e, 0), mass=m_e,
#                   charge=-e, color=color.red)
electron: sphere = sphere(pos=vector(1.4 * a0, 0, 0), radius=0.04 * a0, velocity=vector(0, v_e, 0),
                          mass=m_e, charge=-e, color=color.red, make_trail=True, retain=100)
electron.trail = curve(color=electron.color)


# Defining function for Calculating Acceleration

def acc():
    dr = electron.pos - nucleus.pos
    Force = 1.0 / (4.0 * pi * epsilon) * nucleus.charge * electron.charge / (mag(dr) ** 2) * \
            norm(dr)
    m1 = electron.mass
    return Force / m1


# Defining Order of Time and Time step

t = 0
T_orbit = 2.0 * pi * a0 / v_e
t_end = 1000 * T_orbit
dt = T_orbit / 1000.
print("Time Period in First Orbit= ", T_orbit)

# Updating Position of Electron in loop

while (t < t_end):
    rate(100)
    electron.velocity = electron.velocity + acc() * dt
    electron.pos = electron.pos + electron.velocity * dt
    electron.trail.append(pos=electron.pos)
    t = t + dt
