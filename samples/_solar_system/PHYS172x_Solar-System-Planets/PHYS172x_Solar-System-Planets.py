# https://www.glowscript.org/#/user/PHYS172x/folder/MyPrograms/program/Solar-System-Planets/edit
from vpython import *

# GlowScript 3.0 VPython
# Written by Ergi Bufasi, for PHYS172x.

scene = canvas(width=1000, height=800, background=vector(0., 0., 0.))

SUN = sphere(pos=vector(-50, 30, -30),
             texture="https://upload.wikimedia.org/wikipedia/commons/b/b4/The_Sun_by_the_Atmospheric_Imaging_Assembly_of_NASA%27s_Solar_Dynamics_Observatory_-_20100819.jpg",
             flipx=False, shininess=0.9, radius=7)
label(pos=vector(-50, 20, -30), text='Sun')

Mercury = sphere(pos=vector(-18, 9, 0),
                 texture="https://upload.wikimedia.org/wikipedia/commons/3/30/Mercury_in_color_-_Prockter07_centered.jpg",
                 radius=3)
label(pos=vector(-18, 3.5, 0), text='Mercury')
label(pos=vector(-18, 15, 0), text='θ = 0°', box=False)
label(pos=vector(-18, 13.5, 0), text='58d 15.5h', box=False)

Venus = sphere(pos=vector(-6, 9, 0),
               texture="https://upload.wikimedia.org/wikipedia/commons/1/19/Cylindrical_Map_of_Venus.jpg",
               opacity=0.7, emissive=True, radius=3)
label(pos=vector(-6, 3.5, 0), text='Venus')
label(pos=vector(-6, 15, 0), text='θ = 177.3°', box=False)
label(pos=vector(-6, 13.5, 0), text='243d 26m', box=False)

Earth = sphere(pos=vector(6, 9, 0), texture=textures.earth, radius=3)
label(pos=vector(6, 3.5, 0), text='Earth')
label(pos=vector(6, 15, 0), text='θ = 23.4°', box=False)
label(pos=vector(6, 13.5, 0), text='23h 56m', box=False)

Mars = sphere(pos=vector(18, 9, 0),
              texture="https://upload.wikimedia.org/wikipedia/commons/0/02/OSIRIS_Mars_true_color.jpg",
              opacity=0.7, emissive=True, radius=3)
label(pos=vector(18, 3.5, 0), text='Mars')
label(pos=vector(18, 15, 0), text='θ = 25.2°', box=False)
label(pos=vector(18, 13.5, 0), text='1d 36m', box=False)

Jupiter = sphere(pos=vector(-18, -7, 0),
                 texture="https://upload.wikimedia.org/wikipedia/commons/e/e2/Jupiter.jpg",
                 opacity=0.7, emissive=True, radius=3)
label(pos=vector(-19, -12.5, 0), text='Jupiter')
label(pos=vector(-19, -1, 0), text='θ = 3.1°', box=False)
label(pos=vector(-19, -2.5, 0), text='9h 55m', box=False)

Saturn = sphere(pos=vector(-6, -7, 0),
                texture="https://upload.wikimedia.org/wikipedia/commons/b/b4/Saturn_%28planet%29_large.jpg",
                opacity=0.7, emissive=True, radius=3)
label(pos=vector(-6, -12.5, 0), text='Saturn')
label(pos=vector(-6, -1, 0), text='θ = 26.7°', box=False)
label(pos=vector(-6, -2.5, 0), text='10h 40m', box=False)
Saturnring = ring(pos=vector(-6, -7, 0), axis=vector(2, -3, 0), radius=6, thickness=0.09,
                  texture="https://upload.wikimedia.org/wikipedia/commons/b/b4/Saturn_%28planet%29_large.jpg")
Saturnring = ring(pos=vector(-6, -7, 0), axis=vector(2, -3, 0), radius=6.5, thickness=0.07,
                  texture="https://upload.wikimedia.org/wikipedia/commons/b/b4/Saturn_%28planet%29_large.jpg")
Saturnring = ring(pos=vector(-6, -7, 0), axis=vector(2, -3, 0), radius=5.5, thickness=0.07,
                  texture="https://upload.wikimedia.org/wikipedia/commons/b/b4/Saturn_%28planet%29_large.jpg")

Uranus = sphere(pos=vector(6, -7, 0),
                texture="https://upload.wikimedia.org/wikipedia/commons/3/3d/Uranus2.jpg",
                opacity=0.7, emissive=True, radius=3)
label(pos=vector(6, -12.5, 0), text='Uranus')
label(pos=vector(6, -1, 0), text='θ = 97.8°', box=False)
label(pos=vector(6, -2.5, 0), text='17h 14m', box=False)

Neptune = sphere(pos=vector(18, -7, 0),
                 texture="https://upload.wikimedia.org/wikipedia/commons/5/56/Neptune_Full.jpg",
                 opacity=0.7, emissive=True, radius=3)
label(pos=vector(18, -12.5, 0), text='Neptune')
label(pos=vector(18, -1, 0), text='θ = 28.3°', box=False)
label(pos=vector(18, -2.5, 0), text='16h', box=False)

theta1 = 0.00350
theta2 = 0.00244
theta3 = 0.0408
theta4 = 0.0439
theta5 = 0.0541
theta6 = 0.0460
theta7 = 0.0750
theta8 = 0.0490

t = 0
dt = 0.01

while t < 10:
    rate(20)
    Mercury.rotate(angle=theta1, axis=vector(0, 1, 0), origin=Mercury.pos)
    Venus.rotate(angle=theta2, axis=vector(0, 1, 0), origin=Venus.pos)
    Earth.rotate(angle=theta3, axis=vector(0, 1, 0), origin=Earth.pos)
    Mars.rotate(angle=theta4, axis=vector(0, 1, 0), origin=Mars.pos)
    Jupiter.rotate(angle=theta5, axis=vector(0, 1, 0), origin=Jupiter.pos)
    Saturn.rotate(angle=theta6, axis=vector(0, 1, 0), origin=Saturn.pos)
    Uranus.rotate(angle=theta7, axis=vector(0, 1, 0), origin=Uranus.pos)
    Neptune.rotate(angle=theta8, axis=vector(0, 1, 0), origin=Neptune.pos)
    t = t + dt
