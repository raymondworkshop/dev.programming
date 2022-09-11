"""
TODO
ch7 - Functions as First-Class Objects
"""

import time

# high-order function, no difference between function and data

# the concept of lazy or delayed evaluatoin
# after() function "calls back" to the func() function supplied as an argument
#
# closure
# when a function is passed as data, the related to the environment is carried
class CallbackError(Exception):
    pass

def after(seconds, func, *args):
    time.sleep(seconds)
    try:
        return func(*args)
    except Exception as err:
        raise CallbackError('Call back function failed') from err

def greeting():
    print("Hello World")

# make_greeting() function doesn't carry out any computations
# it creates and returns a function greeting() that does the actual work;
# this only happens when that function gets evaluated later  
def make_greeting(name):
    def greeting():
        print('Hello', name)
    return greeting


# 5.18 Decorators
def main():
    name = 'Guido'
    try:
        r = after(1, greeting)
    except CallbackError as err:
        print("It failed. Reason", err.__cause__)
    #
    f = make_greeting('Guido')
    g = make_greeting('Ada')
    f()
    g()


if __name__ == "__main__":
    main()
