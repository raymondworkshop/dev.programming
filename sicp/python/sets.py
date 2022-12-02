#2.9.3 Sets


#from link import Link

# sets as unordered sequences  
# a set is as a sequence in which no element appears more than ones
# and the empty set is represented by the empty sequence 
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

def set_contains(s, v):
    #"""return True if and only if set s contains v."""
    if s is Link.empty:
        return False
    elif s.first == v:
        return True
    else:
        return set_contains(s.rest, v)


#from tree import Tree
# sets as binary search trees  
# ordered-list representation by arranging the set elements in the form of a tree with two branches
#
class Tree:
    def __init__(self, label, right=None, left=None):
        self.label = label
        if right is not None:
            isinstance(right, Tree)
        if left is not None:
            isinstance(left, Tree)
        self.right = right
        self.left = left

    def __repr__(self):
        if self.right or self.left:
            return 'Tree({0}, {1}, {2})'.format(self.label, repr(self.right), repr(self.left))
        else:
            return 'Tree({0})'.format(repr(self.label))

def set_tree_contains(s, v):
    if s is None:
        return False
    elif s.label == v:
        return True
    elif s.label < v:
        return set_tree_contains(s.right, v)
    elif s.label > v:
        return set_tree_contains(s.left, v)


def adjoin_set(s, v):
    """adjoin an item v to a set s""" 
    if s is None:
        # construct a tree
        return Tree(v)
    elif s.label == v:
        return s
    elif s.label < v:
        return Tree(s.label, s.left, adjoin_set(s.right, v))
    elif s.label > v:
        return Tree(s.label, adjoin_set(s.left, v), s.right)



def main():
    # link List
    s = Link(3, Link(4, Link(5)))
    print(set_contains(s, 2))

    #tree
    st = adjoin_set(adjoin_set(adjoin_set(None, 2), 3), 1)
    print(st)
    print(set_tree_contains(st, 5))
    

if __name__ == "__main__":
    main()