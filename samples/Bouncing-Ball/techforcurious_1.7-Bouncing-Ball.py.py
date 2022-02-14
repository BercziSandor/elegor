from vpython import *

# GlowScript 2.9 VPython
eh_rug = 1.0
width = 10.0

# flower
# granite
# gravel
# earth
# metal
# rock
# rough
# rug
# stones
# stucco
# wood
# wood_old
# gravel
# rock
# stones
# stucco
# wood_old

box_opacity = 0.3
box_texture = textures.gravel
box_color = color.green
ball = sphere(pos=vector(0, 10, 0), radius=1, shininess=0.8,
              color=color.blue)
floor_b = box(pos=vector(0, 0 - 0.1, 0), size=vector(width, 0.1, width), color=box_color,
              opacity=box_opacity, texture=box_texture)
floor_l = box(pos=vector(-(width * 0.5), width * 0.5, -(width * 0.0)), size=vector(0.1, width,
                                                                                   width), \
              color=box_color,
              opacity=box_opacity, texture=box_texture)
floor_r = box(pos=vector(+(width * 0.5), width * 0.5, -(width * 0.0)), size=vector(0.1, width,
                                                                                   width), \
              color=box_color,
              opacity=box_opacity, texture=box_texture)

ball.velocity = vector(3.0, 0, 0)

arr_x = arrow(pos=vector(0, 0, 0), axis=vector(1, 0, 0), shaftwidth=0.1, color=color.red)
arr_y = arrow(pos=vector(0, 0, 0), axis=vector(0, 1, 0), shaftwidth=0.1, color=color.green)
arr_z = arrow(pos=vector(0, 0, 0), axis=vector(0, 0, 1), shaftwidth=0.1, color=color.blue)

dt = 0.01
t = 0
g = -9.8
while (t < 30):
    rate(100)
    ball.velocity.y = ball.velocity.y + g * dt
    ball.pos = ball.pos + ball.velocity * dt
    v1 = ball.pos.x
    v2 = floor_b.pos.x + ball.radius
    v3 = ball.pos.x + ball.radius
    v4 = floor_b.size.x
    if abs(ball.pos.x) > floor_b.size.x / 2 - ball.radius:
        ball.velocity.x = - ball.velocity.x
        print("x fordulás!")

    if ball.pos.y < floor_b.pos.y + 1.25:
        print("y fordulás!")
        ball.velocity.y = - ball.velocity.y * eh_rug
    t = t + dt
