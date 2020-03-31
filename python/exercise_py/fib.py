"""
efficiency in views of time and space
"""
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

# how many times fib(n) is called
def count(f):
    def counted(*args): # optional arg
        counted.call_count += 1
        return f(*args)
    counted.call_count = 0
    return counted


def trace(fn):
    def wrapped(x):
        print('-> ', fn, '(', x, ')')
        return fn(x)
    return wrapped

@trace
def triple(x):
    return 3 * x

if __name__ == "__main__":
    #triple(12)
    #
    fib(5)
    #
    
    