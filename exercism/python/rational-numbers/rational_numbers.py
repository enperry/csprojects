from __future__ import division


class Rational:
    def __init__(self, numer, denom):
        if(denom == 0):
            raise ValueError("denominator can't be zero")
        if(numer * denom > 0):
            numer = abs(numer)
        else:
            numer = -abs(numer)
        denom = abs(denom)
        divisor = gcd(numer, denom)
        self.numer = numer / divisor
        self.denom = denom / divisor

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return Rational(self.numer * other.denom + other.numer * self.denom, self.denom * other.denom)

    def __sub__(self, other):
        return Rational(self.numer * other.denom - other.numer * self.denom, self.denom * other.denom)

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        return Rational(self.numer * other.denom, self.denom * other.numer)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        return Rational(self.numer ** power, self.denom ** power)

    def __rpow__(self, base):
        return (base ** (self.numer ** 1 / self.denom))

def gcd(a, b):
    while(b != 0):
        a, b = b, a % b
    return a