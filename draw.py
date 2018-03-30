"""
Exercise on Classes and Objects from Think Python Edition 2

Exercise 15.2

"""

import turtle

from Point import Point, Rectangle
from Circle import Circle

import polygon

def draw_circle(t, circle):
    """
    draws a circle
    """
    t.pu()
    t.goto(circle.center.x, circle.center.y)
    t.fd(circle.radius)
    t.lt(90)
    t.pd()
    polygon.circle(t, circle.radius)

def draw_rect(t, rect):
    """
    draws a rectangle
    """
    t.pu()
    t.goto(rect.corner.x, rect.corner.y)
    t.setheading(0) # set orientation to east (90north;180 west;270 south)
    t.pd()

    for length in rect.width, rect.length, rect.width, rect.length:
        t.fd(length)
        t.rt(90)


if __name__ == '__main__':
    bob = turtle.Turtle()

    #draw the axes
    length = 400
    bob.fd(length)
    bob.bk(length)
    bob.lt(90)
    bob.fd(length)
    bob.bk(length)

    #draw circle
    circle = Circle()
    circle.center = Point()
    circle.center.x = 150
    circle.center.y = 100
    circle.radius = 75

    draw_circle(bob, circle)

    #draw rectangle
    box = Rectangle()
    box.width = 100
    box.length = 200
    box.corner = Point()
    box.corner.x = 50
    box.corner.y = 50

    draw_rect(bob, box)

    #wait for user to close the windows
    turtle.mainloop()
