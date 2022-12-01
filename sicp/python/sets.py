#2.9.3 Sets


from link import Link

# sets as unordered sequences  
# a set is as a sequence in which no element appears more than ones
# and the empty set is represented by the empty sequence 

def set_contains(s, v):
    #"""return True if and only if set s contains v."""
    if s is Link.empty:
        return False
    elif s.first == v:
        return True
    else:
        return set_contains(s.rest, v)

#

def main():
    s = Link(3, Link(4, Link(5)))
    print(set_contains(s, 2))
    

if __name__ == "__main__":
    main()