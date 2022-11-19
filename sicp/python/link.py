#
# It is A linked list if it is empty or a (first, rest) pair.
# note: link is a **constructor** and first 
# and rest are **selectors** for an abstract data representation of linked list
#
def is_link(s):
    """ s is a linked list if it is empty or a (first, rest) pair.
    """
    return s == "empty" or (len(s) == 2 and is_link(s[1]))

def link(first, rest):
    """ construct a linked list from its 1st element and the rest"""
    assert is_link(rest), "rest must be a linked list"
    return [first, rest]

def first(s):
    """ return the 1st element of a linked list s.
    """
    assert is_link(s), "first only applies to linked lists."
    assert s != "empty"
    return s[0]

def rest(s):
    """ return the rest element of a linked list s"""
    assert is_link(s), "rest only applies to linked list."
    assert s != "empty", "empty linked list has no rest"
    return s[1]



# A linked list is a sequence: it has a finite length and supports element selection by index 
# Linked List Class
class Link:
    """ A linked list with a first element and the rest"""
    empty = ()
    def __init__(self, first, rest=empty):
        # the empty list is a special case of a linked list 
        # that has no first element or rest
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        if i==0:
            return self.first
        else:
            return self.rest[i-1]

    def __len__(self):
        return 1 + len(self.rest)

    
    def __repr__(self):
        if self.rest is Link.empty:
            rest = ''
        else:
            rest = ', ' + repr(self.rest)
        return 'Link({0}{1})'.format(self.first, rest)
    


def link_expression(s):
    """return a string that would evaluate to s"""
    if s.rest is Link.empty:
        rest = ''
    else:
        rest = ', ' + link_expression(s.rest)
    return 'Link({0}{1})'.format(s.first, rest)

# note: recursive functions are particularly well-suited to manipulate linked lists
def extend_link(s,t):
    """return a linked list containing the elements of one Link instance s followed by the elements of another Link instance t """
    if s is Link.empty:
        return t
    else:
        return Link(s.first, extend_link(s.rest, t))


# note: the combination of map_link and filter_link can express 
#  the same logic as a list comprehension
# map 
def map_link(f, s):
    """apply a function f to each element of a linked list s"""
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first), map_link(f, s.rest))

# filter
def filter_link(f, s):
    """return a linked list containing all elements of a linked list s 
    for which f returns a true value"""
    if s is Link.empty:
        return s
    else:
        filtered = filter_link(f, s.rest)
        if f(s.first):
            return Link(s.first, filtered)
        else:
            return filtered

def main():
    # note: Linked lists are particularly useful when constructing sequences incrementally
    four = link(1, link(2, link (3, link(4, "empty"))))
    print(first(four))
    print(rest(four))
    #
    s = Link(3, Link(4, Link(5)))
    print(s[0])
    #Link.__repr__ = link_expression
    print("link list expression:")
    print(s)

    # add
    print("link list add:")
    Link.__add__ = extend_link
    print(s+s)

    # map
    import numpy
    print(map_link(numpy.square, s))
    
    # a list comprehension
    print("link list comprehension:")
    odd = lambda x: x % 2 == 1
    l = map_link(numpy.square, filter_link(odd, s))
    print(l)
    ll = [numpy.square(x) for x in [3,4,5] if odd(x)]
    print(ll)


if __name__ == "__main__":
    main()

