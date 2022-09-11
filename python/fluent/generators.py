"""
TODO
ch8 - Generators
"""

def countdown(n):
    print('Counting down from', n)
    while n > 0:
        yield n #yield keyword defines a generator object 
        n -= 1

def main():
    c = countdown(10)
    next(c)

if __name__ == "__main__":
    main()