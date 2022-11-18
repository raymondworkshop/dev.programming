#
#a linked list is **a pair** containing the first, and the rest
#note: link is a **constructor** and first and rest are **selectors** for an abstract data representation of linked list
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


# A linked list is a sequence:
# it has a finite length and supports element selection by index
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
        return 'Link({0}{1})'.format(s.first, rest)


def link_expression(s):
    """return a string that would evaluate to s"""
    if s.rest is Link.empty:
        rest = ''
    else:
        rest = ', ' + link_expression(s.rest)
    return 'Link({0}{1})'.format(s.first, rest)


if __name__ == "__main__":
    four = link(1, link(2, link (3, link(4, "empty"))))
    print(first(four))
    print(rest(four))
    #
    s = Link(3, Link(4, Link(5)))
    print(s[0])
    #Link.__repr__ = link_expression
    print(s)