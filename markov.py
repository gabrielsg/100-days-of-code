"""
Markov analysis
"""

import os
import sys
import random

#suffix_map = {}
#prefix = ()

class Markov:

    def __init__(self):
        self.suffix_map = {}
        self.prefix = ()

    def process_file(self, filename, order=2):
        """
        reads a file and perform Markov analysis
        filename : string
        order : integer

        returns : map from prefix a list of possible suffix
        """
        fp = open(filename)
        for line in fp:
            for word in line.rstrip().split():
                self.process_word(word, order)

    def process_word(self, word, order=2):
        if len(self.prefix) < order:
            self.prefix += (word,)
            return

        try:
            self.suffix_map[self.prefix].append(word)
        except KeyError:
            self.suffix_map[self.prefix] = [word]

        self.prefix = self.shift(self.prefix, word)

    def shift(self, t, word):
        return t[1:] + (word, )

    def random_text(self, n):
        start = random.choice(list(self.suffix_map.keys()))

        for i in range(n):
            suffixes = self.suffix_map.get(start, None)
            if suffixes == None:
                self.random_text(n-i)
                return

            word = random.choice(suffixes)
            print(word, end=' ')
            start = self.shift(start, word)

def main(script, filename, n=100, order=2):
    try:
        n = int(n)
        order = int(order)
    except ValueError:
        print('Usage: %d filename [# of words] [prefix length]' % script)
    else:
        markov = Markov()
        markov.process_file(filename, order)
        markov.random_text(n)
        print()

if __name__ == '__main__':
    main(*sys.argv)

