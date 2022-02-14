# from vpython import *

# https://www.glowscript.org/docs/VPythonDocs/index.html
# https://www.glowscript.org/docs/VPythonDocs/vector.html
#  mag(A) = A.mag   the magnitude of a vector
#  hat(A) = A.hat   a unit vector in the direction of the vector

from math import asin, sin, cos

from vpython import canvas, arrow, vector, label, color, sphere, rotate, rate, mag

# class constant():
#     def __init__(self, name, symbol, value, unit):
#         self.name = name
#         self.symbol = symbol
#         self.value = value
#         self.unit = unit
#
#
# speed_of_light = constant('speed of light in vacuo', '𝑐', 3.00 * 10 ** 8, 'ms^-1')
# permeability_of_free_space = constant('permeability of free space', '𝜇', 4 * math.pi * 10 ** -7,
#                                       'Hm^-1')
# permittivity_of_free_space = constant('permittivity of free space', '𝜀', 8.85 * 10 ** -12, 'Fm^-1')
# electron_charge = constant('magnitude of the charge of electron', '𝑒', 1.6 * 10 ** -19, 'C')
# Planck_const = constant('the Planck constant', 'ℎ', 6.63 * 10 ** -34, 'Js')
# grav_const = constant('gravitational constant', '𝐺', 6.67 * 10 ** -11, 'Nm2kg^-2')
# Avogadro_const = constant('the Avogadro constant', '𝑁A', 6.02 * 10 ** 23, 'mol^-1')
# mol_gas_const = constant('molar gas constant', '𝑅', 8.31, 'JK^-1mol^-1')
# Boltzmann_const = constant('the Boltzmann constant', '𝑘', 1.38 * 10 ** -23, 'JK^-1')
# Stefan_const = constant('the Stefan constant', 'σ', 5.67 * 10 ** -8, 'Wm^-2K^-4')
# Wien_const = constant('the Wien constant', '𝛼', 2.90 * 10 ** -3, 'mK')
# electron_mass = constant('electron rest mass(equivalent to 5.5×10^-4 u)', '𝑚e', 9.11 * 10 ** -31,
#                          'kg')
# electron_charge_mass = constant('electron charge/mass ratio', '𝑒𝑚e', 1.76 * 10 ** 11, 'Ckg^-1')
# proton_mass = constant('proton rest mass(equivalent to 1.00728u)', '𝑚p', 1.67333 * 10 ** -27, 'kg')
# proton_charge_mass = constant('proton charge/mass ratio', '𝑒𝑚p', 9.58 * 10 ** 7, 'Ckg^-1')
# neutron_mass = constant('neutron rest mass(equivalent to 1.00867u)', '𝑚n', 1.6755 * 10 ** -27,
#                         'kg')
# gravitational_field_strength = constant('gravitational field strength', '𝑔', 9.81, 'Nkg^-1')
# acceleration_due_to_gravity = constant('acceleration due to gravity', '𝑔', 9.81, 'ms^-2')
# atomic_mass = constant('atomic mass unit(1u is equivalent to 931.5MeV)', 'u', 1.661 * 10 ** -27,
#                        'kg')

# https://www.physicsforums.com/threads/vectors-along-surface-of-a-sphere.528248/
# v = vector(3, 3, 3)
# k = vector(0, 0, 1)
# w = cross(k, v)
# d = cross(w, v)
# d = d / mag(d)


show_axis = True
outer_sphere_r = 1
g_r = outer_sphere_r / 8
g_m = 1.0
g_count = 1
grav = 9.81
grav_v = vector(0, -1 * grav, 0)
pi = 2 * asin(1.0)

outer_sphere = None
gs = []

scene = canvas(width=1200, height=500)
scene.autoscale = True

d = outer_sphere_r - g_r
if show_axis:
    arr_len = 1.0
    arr_x = arrow(pos=vector(0, 0, 0), axis=vector(arr_len, 0, 0), shaftwidth=arr_len / 20,
                  color=color.red)
    arr_x_l = label(pos=arr_x.axis, text='x', xoffset=2)

    arr_y = arrow(pos=vector(0, 0, 0), axis=vector(0, arr_len, 0), shaftwidth=arr_len / 20,
                  color=color.green)
    arr_y_l = label(pos=arr_y.axis, text='y', xoffset=2)

    arr_z = arrow(pos=vector(0, 0, 0), axis=vector(0, 0, arr_len), shaftwidth=arr_len / 20,
                  color=color.blue)
    arr_z_l = label(pos=arr_z.axis, text='z', xoffset=2)

outer_sphere = sphere(pos=vector(0, outer_sphere_r, 0), radius=outer_sphere_r, shininess=0.1,
                      color=color.blue, opacity=0.2)
print(f"Outer sphere: {outer_sphere.pos}, radius: {outer_sphere.radius}")

pos_first = vector(d, outer_sphere_r, 0)

for index in range(g_count):
    a = 2 * 3.14 / g_count * index
    pos = rotate(pos_first, angle=a, axis=vector(0, 1, 0))
    g = sphere(pos=pos, radius=g_r, shininess=0.8,
               color=color.red, opacity=0.5)
    g.v = vector(0, 0, 0)
    g.mass = g_m
    g.index = index
    gs.append(g)


def correct_pos(g: sphere, outer_sphere: sphere):
    pass


t = 0.0
dt = 0.01
history = {}


def format_perc(p: float):
    return format(p * 100, ".2f")


def format_vector(v: vector):
    return "[{},{},{}], mag: {}".format(format(v.x, '.2f'), format(v.y, '.2f'), format(v.z,
                                                                                       '.2f'),
                                        format(mag(v), '.2f'))


class golyobis(sphere):
    outer_sphere: sphere


while t < 10:
    rate(10)
    for g in gs:
        tav = g.pos - outer_sphere.pos
        perc = format_perc(mag(tav) / d)
        # https://i.stack.imgur.com/PIVYu.jpg
        # angle of the
        # radial force is zero.
        # tangential force

        theta = tav.diff_angle(-outer_sphere.pos)
        theta_grad = theta * 180 / pi
        a = sin(theta) * grav
        print(
            "[{}] pos: {}[m], v:{}m/s {}%, g_eff={}".format(format(t, '.2f'), format_vector(g.pos),
                                                            format_vector(g.v), perc,
                                                            format(a, '.2f')))

        sin_t = sin(theta)
        cos_t = cos(theta)
        force_grav = grav_v
        force_per = tav.hat * cos(theta)
        force_tens = - force_per

        force_eredo = force_grav + force_tens
        a_eredo = force_eredo / g.mass
        v_old = g.v
        g.v += a_eredo * dt
        print(f" v: {format_vector(v_old)} -> "
              f"{format_vector(g.v)}")
        pos_new = g.pos + g.v * dt
        tav_new = pos_new - outer_sphere.pos
        if mag(tav_new) > d:
            perc = format_perc(mag(tav_new) / d)
            print(f" Correction needed: too far from center: {perc}%")
            #  mag(A) = A.mag   the magnitude of a vector
            #  hat(A) = A.hat   a unit vector in the direction of the vector
            pos_new = outer_sphere.pos + tav_new.hat * d
            angle_corr = pi / 2 - g.v.diff_angle(pos_new - outer_sphere.pos)
            angle_korr_grad = angle_corr * 180 / pi
            g.v = g.v.rotate(angle=angle_corr, axis=vector(0, 0, 1))
            print(f"  New position: {format_vector(pos_new)} ({format_vector(g.pos)})")
            # V correction
            # time.sleep(0.5)

        g.pos = pos_new
        if (t - int(t) < 0.001):
            history[t] = gs
        t = t + dt
pass
