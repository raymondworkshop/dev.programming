"""
ch12
"""

from array import array
import reprlib

# import pytest


class Vector:
    typecode = "d"

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find("[") : -1]
        return f"Vector({components})"

    def __str__(self):
        return str(tuple(self))

    # to allow iteration, return an iterator
    def __iter__(self):
        return iter(self._components)


def test_Vector():
    v = Vector(range(5))
    print(v)

    return


if __name__ == "__main__":
    test_Vector()
