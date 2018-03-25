"""
Exercises from Chapter 15 of Think Complexity 2nd Edition

Lesson : Classes and objects

"""
import math, copy

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

class Rectangle:
    """
    Represent a rectangle

    attributes : width, length, corner
    """
def move_rectangle(rect, dx, dy):
    """
    move a rectangle by changing its corner
    """
    rect.corner.x += dx
    rect.corner.y += dy

def move_rectangle_copy(rect, dx, dy):
    """
    Move rectangle and return a new Rectangle
    """
    new = copy.deepcopy(rect)
    move_rectangle_copy(new, dx, dy)
    return new

def main():
    blank = Point()
    blank.x = 0
    blank.y = 0
    point = Point()
    point.x = 3
    point.y = 4

    print('distance', end=' ')
    print(distance_between_point(blank, point))

    box = Rectangle()
    box.width = 50
    box.length = 100
    box.corner = Point()
    box.corner.x = 5 
    box.corner.y = 10

    print('%g, %g' % (box.corner.x, box.corner.y))
    print('move')
    move_rectangle(box, 20, 40)
    print('%g, %g' % (box.corner.x, box.corner.y))












if __name__ == "__main__":
    main()
