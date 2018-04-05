"""
Classes and Methods
Chapter 17 from Think Python 2nd Editoin
"""

class Time():
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%2d:%2d:%2d' % (self.hour, self.minute, self.second)

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

    def print_time(self):
        print(str(self))

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    #operator overloading +
    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    # right side add, to make the addition operator commutative
    def __radd__(self, other):
        return self.__add__(other)

def int_to_time(seconds):
    """
    makes a new Time object from seconds
    """

    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    time = Time(hour, minute, second)
    return time


def main():
    time = Time()
    time.print_time()
    time1= Time(12, 45, 30)
    print(time1)

    start = Time(9, 45)
    duration = Time(1, 35)
    print(start + duration)

    print(start + 1337)

    print(4000 + start) # add is commutative because of __radd__ 


if __name__ == '__main__':
    main()
