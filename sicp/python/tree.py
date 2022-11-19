"""
Tree - ch2.3.6

Closure as a means of combination

A tree has a root label and a sequence of branches that are also trees
"""

#
# note: the data abstraction for a tree consists of
#  the constructor *tree* and the selectors *label* and *branches*
def tree(root_label, branches=[]):
    for branch in branches:
        assert istree(branch), 'branches must be trees'
    return [root_label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

# a tree is well-formed only if it has a root label and all branches are also trees
def istree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not istree(branch):
            return False
    return True

# check whether or not a tree has branches
def isleaf(tree):
    return not branches(tree)


# Trees can be represented by instances of user-defined classes  
# A tree is any data structure that has a root label and a sequence of branches that are also trees
#
# define trees that have internal values called label at the roots of each subtree
class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = branches

    def __repr__(self):
        if self.branches:
            return 'Tree({0}, {1})'.format(self.label, repr(self.branches))
        else:
            return 'Tree({0})'.format(repr(self.label))
    
    def is_leaf(self):
        return not self.branches
    

def main():
    t = tree(3, [tree(1), tree(2, [tree(1), tree(1)] )])
    print(t)
    #
    t1 = Tree(1, [Tree(3, [Tree(4)]), Tree(2)])
    print(t1)

    


if __name__ == "__main__":
    main()