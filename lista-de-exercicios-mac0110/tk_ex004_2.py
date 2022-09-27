import turtle
import math

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, radius, angle):
    arc_length = 2 * math.pi * radius * abs(angle) / 360
    n = int(arc_length/4) + 3
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t, n, step_length, step_angle)

def petal(t, r, angle):
    """Draws a petal using two arcs.

    t: Turtle
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)


def flower(t, n, r, angle):
    """ Draws a flower.

    t: turtle
    n: number of petals
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(n):
        petal(t, r, angle)
        t.lt(360 / n)

bob = turtle.Turtle(visible=False)
flower(bob, 7, 200, 45)
turtle.mainloop()
