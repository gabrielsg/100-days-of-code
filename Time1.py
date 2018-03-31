"""
This module contains exercises taken from Chapter 16 of
Think Python 2
Classes and Functions

"""
class Time():
    """
    Represents time of day
    attributes : hour, min, sec
    """


def print_time(t):
    print('%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second))


def is_after(t1, t2):
    """
    returns True if t1 comes after t2, otherwise false
    """
    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)
    #tuple comparison

def increment(time, second):
    """
    functional programming
    doesn't change the object it gets as parameters
    """
    new = Time()
    new.second = time.second + second
    new.minute = time.minute
    new.hour = time.hour
    if new.second >= 60:
        new.second -= 60
        new.minute += 1
    return new

def increment1(time, second):
    """
    new version of increment with using time to int
    and second_to_int
    """
    second += time_to_int(time)
    return int_to_time(second)


def time_to_int(time):
    """
    convert time to integers (seconds)
    """
    minutes = time.hour * 60 + time.minute
    seconds = minutes*60 + time.second
    return seconds

def int_to_time(seconds):
    """
    convert seconds to time
    use divmod which divide first arguement with second
    and returns quotient and remainder as a tuple
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def valid_time(time):
    if time.hour <  0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True


def add_times(t1, t2):
    assert valid_time(t1) and valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

def mul_time(t1, x):
    assert valid_time(t1)
    seconds = time_to_int(t1) * x
    return int_to_time(seconds)
    

def main():
    time = Time()
    time.hour = 11
    time.minute = 30
    time.second = 45


    print_time(time)

    time2 = Time()
    time2.hour = 11
    time2.minute = 35
    time2.second = 45

    print(is_after(time, time2))

    print_time(increment(time2, 20))

    print(time_to_int(time))

    seconds = 41445
    print_time(int_to_time(seconds))

    print_time(increment(time, 30))

    #explore assert statement
    print_time(add_times(time, time2))

    #pace
    time3 = Time()
    time3.hour = 3
    time3.minute = 45
    time3.second = 30
    distance = 42  #km
    pace = mul_time(time3, 1/distance)
    print_time(pace)


if __name__ == '__main__':
    main()

