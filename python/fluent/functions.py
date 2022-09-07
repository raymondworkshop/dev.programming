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
def after(seconds, func):
    time.sleep(seconds)
    func()

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
    after(1, greeting)
    #
    f = make_greeting('Guido')
    g = make_greeting('Ada')
    f()
    g()


if __name__ == "__main__":
    main()
