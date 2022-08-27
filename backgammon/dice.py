import random

class Dice(object):

    def __init__(self):
        self.values = [None, None]

    def __getitem__(self, i):
        return self.values[i]

    def __repr__(self):
        return '<%i,%i>' % tuple(self.values)

    def roll(self):
        self.values = [random.randint(1,6), random.randint(1,6)]

    def is_doubles(self):
        return self.values[0] == self.values[1]
