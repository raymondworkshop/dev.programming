"""
sequence in python
#
note: the use of conventional interfaces 
  - a conventional interface is a data format that is shared across many modular components,
  which can be mixed and matched to perform data processing   
"""

# example 1: sum the even members of the first n Fibonacci numbers  
def fib(k):
    """ compute the kth Fibonacci number
    """
    prev, curr = 1, 0
    for _ in range(k-1):
        prev, curr = curr, prev+curr
    return curr


def sum_even_fib():
    return


if __name__ == "__main__":
    sum_even_fib()