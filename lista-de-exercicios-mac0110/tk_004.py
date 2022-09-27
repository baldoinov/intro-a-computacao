import turtle
import math

def square(t, length):
    """(turtle, float) -> NoneType
    Draws a square with side length "length" using the turtle object t
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360 / n
    polyline(t, n, length, angle)

def circle(t, radius):
    arc(t, radius, 360)

def arc(t, radius, angle):
    arc_length = 2 * math.pi * radius * angle / 360
    n = int(arc_length/3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t, n, step_length, step_angle)

    
bob = turtle.Turtle()
circle(bob, 100)
turtle.mainloop()
