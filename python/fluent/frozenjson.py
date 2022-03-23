"""
ex23-3 - 

properties replace a public data attribute with 
accessor methods (getter/setter) without changing the class interface
"""

#
# note: a user-defined class implementing __getattr__ can implement
#    "virtual attributes" by computing values on the fly whenever somebody
#    tries to read a nonexistent attribute like obj.no_such_attr
#

from collections import abc


class FrozenJSON:
    """navigate a JSON-like object using attribute notation"""

    def __init__(self, mapping):
        self.__data = dict(mapping)

    def __getattr__(self, name):
        try:
            return getattr(self.__data, name)
        except AttributeError:
            return FrozenJSON.build(self.__data[name])

    @classmethod  # for alternative constructors, receiving the class itself instead of an instance
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):  # if obj is a mapping
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):  # if it is a list
            return [cls.build(item) for item in obj]
        else:  # it is a str or an int
            return obj


def main():
    student = FrozenJSON({"name": "Jim Bo", "class": 1982})
    return


if __name__ == "__main__":
    main()
