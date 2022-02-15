"""
TODO
"""
import math
from math import sin, cos

from vpython import canvas, arrow, vector, label, color, sphere, rotate, rate, mag


# https://www.glowscript.org/docs/VPythonDocs/index.html
# https://www.glowscript.org/docs/VPythonDocs/vector.html
#  mag(A) = A.mag   the magnitude of a vector
#  hat(A) = A.hat   a unit vector in the direction of the vector


class Constant():
    """
    TODO: where is it from??
    """

    def __init__(self, name, symbol, value, unit):
        self.name = name
        self.symbol = symbol
        self.value = value
        self.unit = unit

    def __repr__(self):
        return f"{self.value}{self.unit}"


speed_of_light = Constant('speed of light in vacuo', '𝑐', 3.00 * 10 ** 8, 'ms^-1')
permeability_of_free_space = Constant('permeability of free space', '𝜇', 4 * math.pi * 10 ** -7,
                                      'Hm^-1')
permittivity_of_free_space = Constant('permittivity of free space', '𝜀', 8.85 * 10 ** -12, 'Fm^-1')
electron_charge = Constant('magnitude of the charge of electron', '𝑒', 1.6 * 10 ** -19, 'C')
Planck_const = Constant('the Planck constant', 'ℎ', 6.63 * 10 ** -34, 'Js')
grav_const = Constant('gravitational constant', '𝐺', 6.67 * 10 ** -11, 'Nm2kg^-2')
Avogadro_const = Constant('the Avogadro constant', '𝑁A', 6.02 * 10 ** 23, 'mol^-1')
mol_gas_const = Constant('molar gas constant', '𝑅', 8.31, 'JK^-1mol^-1')
Boltzmann_const = Constant('the Boltzmann constant', '𝑘', 1.38 * 10 ** -23, 'JK^-1')
Stefan_const = Constant('the Stefan constant', 'σ', 5.67 * 10 ** -8, 'Wm^-2K^-4')
Wien_const = Constant('the Wien constant', '𝛼', 2.90 * 10 ** -3, 'mK')
electron_mass = Constant('electron rest mass(equivalent to 5.5×10^-4 u)', '𝑚e', 9.11 * 10 ** -31,
                         'kg')
electron_charge_mass = Constant('electron charge/mass ratio', '𝑒𝑚e', 1.76 * 10 ** 11, 'Ckg^-1')
proton_mass = Constant('proton rest mass(equivalent to 1.00728u)', '𝑚p', 1.67333 * 10 ** -27, 'kg')
proton_charge_mass = Constant('proton charge/mass ratio', '𝑒𝑚p', 9.58 * 10 ** 7, 'Ckg^-1')
neutron_mass = Constant('neutron rest mass(equivalent to 1.00867u)', '𝑚n', 1.6755 * 10 ** -27,
                        'kg')
gravitational_field_strength = Constant('gravitational field strength', '𝑔', 9.81, 'Nkg^-1')
acceleration_due_to_gravity = Constant('acceleration due to gravity', '𝑔', 9.81, 'ms^-2')
atomic_mass = Constant('atomic mass unit(1u is equivalent to 931.5MeV)', 'u', 1.661 * 10 ** -27,
                       'kg')

# https://www.physicsforums.com/threads/vectors-along-surface-of-a-sphere.528248/
# v = vector(3, 3, 3)
# k = vector(0, 0, 1)
# w = cross(k, v)
# d = cross(w, v)
# d = d / mag(d)


SHOW_AXIS = True
BIG_SPHERE_RADIUS = 1
SPHERE_RADIUS = BIG_SPHERE_RADIUS / 8
RADIUS_DIFF = BIG_SPHERE_RADIUS - SPHERE_RADIUS
SPHERE_MASS = 1.0
SPHERE_COUNT = 1
GRAV_VECTOR = vector(0, -1 * gravitational_field_strength.value, 0)
# pi = 2 * asin(1.0)


BIG_SPHERE = None
spheres = []

scene = canvas(width=1200, height=500)
scene.autoscale = True

if SHOW_AXIS:
    ARR_LEN = 1.0
    arr_x = arrow(pos=vector(0, 0, 0), axis=vector(ARR_LEN, 0, 0), shaftwidth=ARR_LEN / 20,
                  color=color.red)
    arr_x_l = label(pos=arr_x.axis, text='x', xoffset=2)

    arr_y = arrow(pos=vector(0, 0, 0), axis=vector(0, ARR_LEN, 0), shaftwidth=ARR_LEN / 20,
                  color=color.green)
    arr_y_l = label(pos=arr_y.axis, text='y', xoffset=2)

    arr_z = arrow(pos=vector(0, 0, 0), axis=vector(0, 0, ARR_LEN), shaftwidth=ARR_LEN / 20,
                  color=color.blue)
    arr_z_l = label(pos=arr_z.axis, text='z', xoffset=2)

BIG_SPHERE = sphere(pos=vector(0, BIG_SPHERE_RADIUS, 0), radius=BIG_SPHERE_RADIUS, shininess=0.1,
                    color=color.blue, opacity=0.2)
print(f"Outer sphere: {BIG_SPHERE.pos}, radius: {BIG_SPHERE.radius}")

pos_first = vector(RADIUS_DIFF, BIG_SPHERE_RADIUS, 0)

for index in range(SPHERE_COUNT):
    a = 2 * 3.14 / SPHERE_COUNT * index
    pos = rotate(pos_first, angle=a, axis=vector(0, 1, 0))
    g = sphere(pos=pos, radius=SPHERE_RADIUS, shininess=0.8,
               color=color.red, opacity=0.5)
    g.v = vector(0, 0, 0)
    g.mass = SPHERE_MASS
    g.index = index
    spheres.append(g)


def correct_pos(a_sphere: sphere, outer_sphere: sphere):
    """
    TODO
    """
    return a_sphere, outer_sphere


def format_perc(percent: float):
    """
    TODO
    """
    return format(percent * 100, ".2f")


def format_vector(vect: vector):
    """
    TODO
    """
    coord_x = format(vect.x, '.2f')
    coord_y = format(vect.y, '.2f')
    coord_z = format(vect.z, '.2f')
    length = format(mag(vect), '.2f')
    return f"[{coord_x}, {coord_y}, {coord_z}], mag: {length}"


def main():
    """
    TODO
    """
    time = 0.0
    delta_t = 0.01
    history = {}

    while time < 10:
        rate(10)
        for a_sphere in spheres:
            tav = a_sphere.pos - BIG_SPHERE.pos
            perc = format_perc(mag(tav) / RADIUS_DIFF)
            # https://i.stack.imgur.com/PIVYu.jpg
            # angle of the
            # radial force is zero.
            # tangential force

            theta = tav.diff_angle(-BIG_SPHERE.pos)
            # theta_grad = theta * 180 / math.pi
            acceleration = sin(theta) * gravitational_field_strength

            print(
                f"[{format(time, '.2f')}] pos: {format_vector(a_sphere.pos)}[m], "
                f"v:{format_vector(a_sphere.v)}m/s {perc}%, g_eff={format(acceleration, '.2f')}")

            # sin_t = sin(theta)
            # cos_t = cos(theta)
            force_grav = GRAV_VECTOR
            force_per = tav.hat * cos(theta)
            force_tens = - force_per

            force_eredo = force_grav + force_tens
            a_eredo = force_eredo / a_sphere.mass
            v_old = a_sphere.v
            a_sphere.v += a_eredo * delta_t
            print(f" v: {format_vector(v_old)} -> "
                  f"{format_vector(a_sphere.v)}")
            pos_new = a_sphere.pos + a_sphere.v * delta_t
            tav_new = pos_new - BIG_SPHERE.pos
            if mag(tav_new) > RADIUS_DIFF:
                perc = format_perc(mag(tav_new) / RADIUS_DIFF)
                print(f" Correction needed: too far from center: {perc}%")
                #  mag(A) = A.mag   the magnitude of a vector
                #  hat(A) = A.hat   a unit vector in the direction of the vector
                pos_new = BIG_SPHERE.pos + tav_new.hat * RADIUS_DIFF
                angle_corr = math.pi / 2 - a_sphere.v.diff_angle(pos_new - BIG_SPHERE.pos)
                # angle_korr_grad = angle_corr * 180 / math.pi
                a_sphere.v = a_sphere.v.rotate(angle=angle_corr, axis=vector(0, 0, 1))
                print(f"  New position: {format_vector(pos_new)} ({format_vector(a_sphere.pos)})")
                # V correction
                # time.sleep(0.5)

            a_sphere.pos = pos_new
            if time - int(time) < 0.001:
                history[time] = spheres
            time = time + delta_t


if __name__ == '__main__':
    main()
