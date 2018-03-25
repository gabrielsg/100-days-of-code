"""This module contains excercise related to

Think Python, 2nd Edition
Chapter 15.9 Excercise

"""
import copy
import math
from Point import Point, print_point, Rectangle, distance_between_point, move_rectangle, move_rectangle_copy

class Circle:
    """
    attributes : center, radius
    """

def point_in_circle(circle, point):
    """
    checks if a point is within or on the circle
    """
    d = distance_between_point(point, circle.center)
    return d <= circle.radius

def rect_in_circle(circle, rectangle):
    """
    check if  rectangle is within the  circle
    """

def main():
    c = Circle()
    c.center = Point()
    c.center.x = 150
    c.center.y = 100
    c.radius = 75

    p = Point()
    p.x = 80
    p.y = 100
    print('point', end=' ')
    print_point(p)
    print('point within or on circle', end = ' ')
    print(point_in_circle(c, p))



if __name__ == "__main__":
    main()
