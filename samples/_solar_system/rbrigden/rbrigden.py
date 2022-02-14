# https://gist.github.com/rbrigden/2e94c7ebecce571447dc
# simulate the solar system
# Author: Ryan Brigden
# 33-151: M&I I

# planet and orbital data from:
# http://nssdc.gsfc.nasa.gov/planetary/factsheet/planet_table_ratio.html
# http://education.nationalgeographic.com/activity/planetary-size-and-distance-comparison/
# http://www.sjsu.edu/faculty/watkins/orbital.htm

from vpython import *

scene = canvas(width=800, height=500, background=vector(0.5, 0.5, 0.5))

# mass, orbital velocity & radius of the earth
# initial momentum of earth = me * vE
# distance of the earth from the sun is dE
mE = 5.97e24
vE = 30e3
rE = 2
dE = 149.6e9
GRAVC = 6.67e-11
vscale = 10000


def create_sphere(labl: str, pos: vector, radius, colr: vector, mass, velocity: vector) -> dict:
    planet = sphere(pos=pos, radius=radius, color=colr, mass=mass, label=labl, make_trail=True,
                    retain=1000000)
    planet.velocity = velocity
    return {
        "planet": planet,
        "label": label(pos=planet.pos, text=labl, xoffset=10, yoffset=10),
        "arrow": arrow(pos=planet.pos, axis=planet.velocity * vscale, color=color.red,
                       planet=planet)
    }


# create the solar system
planets = {}

sun = create_sphere(labl="Sun", pos=vector(0, 0, 0), radius=696e6, colr=color.yellow,
                    mass=3.33e5 * mE,
                    velocity=vector(0, 0, 0))
planets.update({"Sun": sun})

mercury = create_sphere(labl="Mercury", pos=vector(0, 0, 0.387 * dE), radius=696e6,
                        colr=color.blue,
                        mass=0.0553 * mE,
                        velocity=vector(1.607 * vE, 0, 0))
planets.update({"Mercury": mercury})

venus = create_sphere(pos=vector(0, 0, 0.723 * dE), radius=696e6, colr=color.cyan,
                      mass=0.815 *
                           mE,
                      labl="Venus", velocity=vector(1.174 * vE, 0, 0))
planets.update({"Venus": venus})

earth = create_sphere(pos=vector(0, 0, dE), radius=696e6, colr=color.green, mass=mE,
                      labl="Earth", velocity=vector(vE, 0, 0))
planets.update({"Earth": earth})

# mars = create_sphere(pos=vector(0, 0, 1.52 * dE), radius=696e6, colr=color.red, mass=0.107 *
#                                                                                      mE,
#                      labl="Mars", velocity=vector(0.802 * vE, 0, 0))
# planets.update({"Mars": mars})

# jupiter = sphere(pos=vector(0, 0, 5.20 * dE), radius=696e6, color=color.yellow, mass=317.8 * mE)
# jupiter.velocity = vector(0.434 * vE, 0, 0)
# planets.append(jupiter)
#
# saturn = sphere(pos=vector(0, 0, 9.58 * dE), radius=696e6, color=color.white, mass=95.2 * mE)
# saturn.velocity = vector(0.323 * vE, 0, 0)
# planets.append(saturn)
#
# uranus = sphere(pos=vector(0, 0, 19.20 * dE), radius=696e6, color=color.orange, mass=14.5 * mE)
# uranus.velocity = vector(0.228 * vE, 0, 0)
# planets.append(uranus)
#
# neptune = sphere(pos=vector(0, 0, 30.05 * dE), radius=696e6, color=color.magenta, mass=17.1 * mE)
# neptune.velocity = vector(0.182 * vE, 0, 0)
# planets.append(neptune)


dt = 100
t = 0


def gravAcc(obj, other):
    """ acceleration of an object due to gravitational force """
    rVector = obj.pos - other.pos
    acc = -((GRAVC * other.mass) / rVector.mag2)
    acc *= rVector.norm()
    return acc


def tell_time(seconds):
    years = int(seconds / 3.15569e7)
    months = int((seconds % 3.15569e7) / 2.62974e6)
    days = int(((seconds % 3.15569e7) % 2.62974e6) / 86400)
    return f"Years: {years} years, {months} months, {days} days"


scene.autoscale = True

# while t < 3.15569e7:
while True:
    # rate(10)
    rate(1e50)
    print(tell_time(t))

    for planet1_ in planets.values():
        planet1 = planet1_["planet"]
        for planet2_ in planets.values():
            planet2 = planet2_["planet"]
            if planet1 != planet2:
                planet1.velocity += gravAcc(planet1, planet2) * dt

    # update the position of the objects
    for planet_ in planets.values():
        planet = planet_["planet"]
        planet.pos += planet.velocity * dt

        arrw: arrow = planet_["arrow"]
        arrw.pos = planet.pos
        arrw.axis = planet.velocity * vscale

        labl: label = planet_["label"]
        labl.pos = planet.pos

    t += dt

# 3.15569e7 in a year
