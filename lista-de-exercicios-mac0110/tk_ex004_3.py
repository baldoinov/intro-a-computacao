import turtle

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360 / n
    polyline(t, n, length, angle)

bob = turtle.Turtle(visible=False)
polygon(bob, 5, 100)