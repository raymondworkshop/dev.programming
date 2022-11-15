"""
Instead of defining and instantiating classes,
use functions for simple interfaces between components in python
   - customize behavior by passing in a function
"""

def sort_names():
    names = ["Socrates", "Archimedes", "Plato", "Aristotle"]
    # the key hook is used by sort API to call back your code while they execute
    names.sort(key=len) #  providing the len built-in function as the key hook 

    print(names)

current = {
        'green': 2,
        'blue': 3
    }

increments = [
    ('red', 5),
    ('blue', 7),
    ('orange', 1),
]

# define a class that provides the __call__ method 
# when we need a function to maintain state
class CountMissing:
    def __init__(self):
        self.added = 0

    # __call__ allows an object to be called just like a function
    def __call__(self):
        self.added = self.added + 1
        return 0

#
def count_keys():
    from collections import defaultdict

    counter = CountMissing()
    assert counter() == 0
    assert callable(counter)

    # note: here the object counter acted like a function 
    # use the function counter as an interfaces between components
    result = defaultdict(counter, current)
    for key, amount in increments:
        result[key] += amount

    print(counter.added)
    assert counter.added == 2



def main():
    sort_names()
    count_keys()

if __name__ == "__main__":
    main()