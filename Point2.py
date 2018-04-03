"""
Class and Method Chapter 17  Think Python, 2nd Edition
"""

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)


def main():
    p = Point()
    print(p)




if __name__ == '__main__':
    main()
