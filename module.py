import random


def float_to_bits(value, depth):
    """
    Converts a float between 0.0 and 1.0 to an integer with a range of (2^depth)-1
    """
    return round(value * ((2**depth) - 1))


class Color(object):
    def __init__(self, *args):
        self.color = (random.uniform(0.0, 1.0), random.uniform(0.0, 1.0), random.uniform(0.0, 1.0))

    def __repr__(self):
        return '({}, {}, {})'.format(*self.color)

    def __str__(self):
        return '({}, {}, {})'.format(*self.color)

    def rgb(self):
        return tuple(float_to_bits(component, 8) for component in self.color)


class ColorSet(object):
    def __init__(self, count):
        self.count = count
        self.colors = [Color() for x in range(count)]

    @property
    def in_rgb(self):
        return [x.rgb() for x in self.colors]