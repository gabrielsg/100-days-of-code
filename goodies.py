"""
Think Python Edition 2
Chapter 19

"""

"""
Conditional Expressions in place of Conditional Statements

"""

import math
#x = 10
#if x > 0:
#    y = math.log(x)
#else:
#    y = float('nan')
#print(y)

#above code can be written
x = 10
y = math.log(x) if x > 0 else float('nan')
print(y)


#factorial
#def factorial(n):
#    if n == 0:
#        return 1
#    else:
#        return n * factorial(n-1)
#print(factorial(4))

def factorial(n):
    return 1 if n == 0 else  n *  factorial(n-1)
print(factorial(4))

#Optional Arguments
#class GoodKangaroo:
#    def __init__(self, name, content=None):
#        self.name = name
#        if content == None:
#            contents = []
#        self.pouch_contents = contents

class GoodKangaroo:
    def __init__(self, name, content=None):
        self.name = name
        self.pouch_cotents = [] if content == None else content


"""
List Comprehensions

"""

#def capitalize_all(t):
#    res = []
#    for s in t:
#        res.append(s.capitalize())
#    return res

#name =  'Gabriel'
#print(capitalize_all(name))

def capitalize_all(t):
    return [s.capitalize() for s in t]

name = 'Gabriel'
print(capitalize_all(name))

#def only_upper(t):
#    res = []
#    for s in t:
#        if s.isupper():
#            res.append(s)
#    return res
#
#n = 'GabrielRodrigues'
#print(only_upper(n))

def only_upper(t):
    return [s for s in t if s.isupper()]

n = 'MaryChong'
print(only_upper(n))

"""
Generator Expressions

"""
g = (x**2 for  x in range(5)) #similar to list but expression in parenthesis instead of bracket
print(g) # result is a generator object that can iterate through a sequence of values

next(g)
next(g)
for val in g:
    print(val)

next(g) #once generator is exhausted, will raise a StopIteration message

"""
Sets
behaves like a collection of Dictionary keys with no values

"""
d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':2, 'd':4}

def substract(d1, d2):
    return set(d1) - set(d2) # returns a set {'b', 'c'}

def has_duplicates(t):
    d = {}
    for x in t:
        if x in d:
            return True
        d[x]= True
    return False

lst = [2, 3, 4, 3]
has_duplicates(lst) #returns True

def has_duplicates1(t):
    return len(set(t)) < len(t)


















