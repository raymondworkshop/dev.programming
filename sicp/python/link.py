#
#a linked list is **a pair** containing the first, and the rest
#note: link is a **constructor** and first and rest are **selectors** for an abstract data representation of linked list
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


if __name__ == "__main__":
    four = link(1, link(2, link (3, link(4, "empty"))))
    print(first(four))
    print(rest(four))