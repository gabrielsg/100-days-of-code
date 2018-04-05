"""
Class and Method Chapter 17  Think Python, 2nd Edition
"""

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)

    def __add__(self, other):
        if isinstance(other, Point):
            return self.add_point(other)
        elif isinstance(other, tuple):
            return self.add_tuple(other)
        else:
            msg = "Point doesn't know how to add type " + type(other)
            raise TypeError(msg)

    def add_point(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def add_tuple(self, other):
        # note tuple element is accessed with square bracket
        return (self.x + other[0], self.y + other[1])

def print_attributes(obj):
    """
    useful method for debugging
    vars is a builtin function that returns a dictionary
    that maps from atttribute names to attribute values
    getattr takes an object and attr and returns attr value
    """
    for attr in vars(obj):
        print(attr, getattr(obj, attr))



def main():
    p = Point(1, 2)
    q = Point(2,4)
    print(p)
    print(q)
    print(p + q)
    print(p + (2,2))

    print_attributes(q)




if __name__ == '__main__':
    main()
