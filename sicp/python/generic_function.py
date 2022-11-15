"""
implementing generic functions: 
   - shared interfaces 
   - type dispatching
   - type coercion  

A system to perform arithmetic operations on complex numbers 
using generic operations
"""

# note: the class requires the Number objects have add and mul methods,
# but does not define them
# 
# serve as a superclass of various specific number classes
class Number:
    #import ipdb; ipdb.set_trace()
    def __add__(self,other):
        return self.add(other)

    def __mul__(self, other):
        return self.mul(other)


def add_complex_and_rational(c, r):
    return ComplexRI(c.real + r.numer/r.denom, c.imag)

def mul_complex_and_rational(c, r):
        r_magnitude, r_angle = r.numer/r.denom, 0
        if r_magnitude < 0:
            r_magnitude, r_angle = -r_magnitude, pi
        return ComplexMA(c.magnitude * r_magnitude, c.angle + r_angle)

def add_rational_and_complex(r, c):
        return add_complex_and_rational(c, r)

def mul_rational_and_complex(r, c):
        return mul_complex_and_rational(c, r)

# Type dispatching
# use the type_tag attribute to distinguish types of arguments
class NewNumber:
    def __add__(self, other):
        if self.type_tag == other.type_tag:
            return self.add(other)

        elif (self.type_tag, other.type_tag) in self.adders:
            return self.cross_apply(other, self.adders)

    def __mul__(self, other):
        if self.type_tag == other.type_tag:
                return self.mul(other)
        elif (self.type_tag, other.type_tag) in self.multipliers:
                return self.cross_apply(other, self.multipliers)

    def cross_apply(self, other, cross_fns):
        cross_fn = cross_fns[(self.type_tag, other.type_tag)]
        return cross_fn(self, other)

    # all cross-type implementations are indexed by pairs of type tags in the adders and multipliers dictionaries
    adders = {
        ("com", "rat"): add_complex_and_rational,
        ("rat", "com"): add_rational_and_complex
    }

    multipliers = {
        ("com", "rat"): mul_complex_and_rational,
        ("rat", "com"): mul_rational_and_complex
    }


# note: An interface is a set of shared attribute names, along with a specification of their behavior
# here the interface needed to implement arithmetic consists of four attributes: real, imag, magnitude, and angle 
#
# define add and mul appropriately for complex numbers
class Complex(NewNumber):
    type_tag = 'com'
    def add(self, other):
        return ComplexRI(self.real + other.real, self.imag + other.imag)
    
    def mul(self, other):
        magnitude = self.magnitude + other.magnitude
        return ComplexMA(magnitude, self.angle + other.angle)


# ComplexRI constructs a complex number from real and imaginary parts
from math import atan2
class ComplexRI(Complex):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    @property
    def magnitude(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5
    @property
    def angle(self):
        return atan2(self.imag, self.real)
    
    def __repr__(self):
        return 'ComplexRI ({0:g}, {1:g})'.format(self.real, self.imag)


# ComplexMA constructs a complex number from a magnitude and angle
from math import sin, cos, pi
class ComplexMA(Complex):
    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle

    @property
    def real(self):
        return self.magnitude * cos(self.angle)
    @property
    def imag(self):
        return self.magnitude * sin(self.angle)

    def __repr__(self):
            return 'ComplexMA({0:g}, {1:g} * pi)'.format(self.magnitude, self.angle/pi)
    

#Rational number like (2.1, 3)
import math
class Rational(Number):
    type_tag = 'rat'
    def __init__(self, numer, denom):
        g = math.gcd(numer, denom)
        self.numer = numer // g
        self.denom = denom // g
    def __repr__(self):
        return 'Rational ({0}, {1})'.format(self.numer, self.denom)

    def add(self, other):
        nx, dx = self.numer, self.denom
        ny, dy = other.numer, other.denom
        return Rational(nx * dy + ny * dx, dx * dy)
    def mul(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        return Rational(numer, denom)


#Complex.type_tag = 'com'
#Rational.type_tag = 'rat'


def main():
    from math import pi
    # 1. Complex.add() is generic, 
    # because it can take either a ComplexRI or ComplexMA as the value for other
    # both ComplexRI and ComplexMA share an interface: attributes- real, imag, magnitude, and angle.
    complex = Complex.add(ComplexRI(1,2), ComplexMA(2, pi/2))
    print(complex)

    #2. Type dispatching -  write functions that inspect the type of arguments they receive,
    # then execute code that is appropriate for those types
    print(ComplexRI(1.5, 0) + Rational(3, 2))

    #3. Coercion -  try to coerce one type into another  

if __name__ == "__main__":
    main()