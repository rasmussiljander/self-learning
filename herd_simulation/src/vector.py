"""Class for handling location, direction information in animation as vectors. Has all important vector operations:
    addition: a+b
    subtraction: a-b
    multiplication:c*a (c = constant)
    setting magnitude, getting unit vector, getting angle of vector between x-axis, printing information"""

import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, a):
        x = self.x + a.x
        y = self.y + a.y
        return Vector(x, y)

    def sub(self, a):
        x = self.x - a.x
        y = self.y - a.y
        return Vector(x, y)

    def mult(self, c):
        x = c * self.x
        y = c * self.y

        return Vector(x, y)

    def get_unit(self):
        mag = self.get_magn()
        try:
            x = self.x / mag
            y = self.y / mag
            return Vector(x, y)

        except ZeroDivisionError:
            return self

    def get_magn(self):
        return math.hypot(self.x, self.y)

    def set_magn(self, magn):
        v = self.get_unit()
        if v.get_magn() == 0:
            x = 0.5 * math.sqrt(2) * magn
            y = x

        else:
            x = v.x * magn
            y = v.y * magn

        v.x = x
        v.y = y

        return v

    def set_limit(self, magn):
        if self.get_magn() > magn:
            return self.set_magn(magn)
        else:
            return self

    def dot_product(self, a):
        return self.x * a.x + self.y * a.y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_degrees(self):
        deg = math.atan2(self.y, self.x)
        deg = math.degrees(deg)
        return deg
