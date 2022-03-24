"""ex 23-9 - TODO
Computing attribute values using property
"""

import json


class Record:  # return a dict with Record instances
    def __init__(self, **kwargs):
        # create a bunch of attributes in the instance
        self.__dict__.update(
            kwargs
        )  # the __dict__ of an object is where its attributes are kept

    def __repr__(self):
        cls_name = self.__class__.__name__
        return f"<{cls_name} serial={self.serial!r}>"


def load(path=None):
    pass


def main():
    pass


if __name__ == "__main__":
    main()
