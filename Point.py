"""
Exercises from Chapter 15 of Think Complexity 2nd Edition

Lesson : Classes and objects

"""
import math

class Point:
    """
    attributes (x, y) representing 2D space
    """

def print_point(p):
    print('%g, %g' % (p.x, p.y))

def distance_between_point(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    d = math.sqrt(dx**2 + dy**2)
    return d

def main():
    blank = Point()
    blank.x = 0
    blank.y = 0
    point = Point()
    point.x = 3
    point.y = 4

    print('distance', end=' ')
    print(distance_between_point(blank, point))



    
if __name__ == "__main__":
    main()
