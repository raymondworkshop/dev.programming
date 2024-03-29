"""
know more about class in python
ch5 - Classed and Interfaces  

ch7 Classes and object-oriented programming in python distilled  
"""


class Account:
    # a class merely hold the methods
    """ 
    A simple bank account
    """
    owner: str
    balance: float 

    def __init__(self, owner, balance): #self is an instance
        self.owner = owner
        self.balance = balance
    
    def __repr__(self):
        return f'Account({self.owner!r}, {self.balance!r})'

    def deposit(self,amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount

    def inquiry(self) -> float:
        return self.balance


class AccountPortfolio:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def total_funds(self):
        return sum(account.inquiry() for account in self.accounts)

    def __len__(self): #len()
        return len(self.accounts)

    def __getitem__(self, index): #indexing
        return self.accounts[index]

    def iter(self): #iteration
        return iter(self.accounts)


def test_Account():
    a = Account('Raymond', 1000.0)
    # call Account.__init__(a, 'Raymond', 1000.0)
    print(vars(a)) #view instance variables

    port = AccountPortfolio()
    port.add_account(a)
    port.add_account(Account('Eva', 50.0))

    print(port.total_funds())
    print(len(port))
    print(port[0]) #indexing
    
    for account in port:
        print(account)


# 7.8 composition  
# prefer composition over inheritance  
# note: Using inheritance gets a lot of features that aren't pertinent to the problem actually being solved 
#  if the object you're building is a specialized version of the parent class, use inheritance;
# or if you are merely using it as a component in building something else, use composition 
#
class Stack:
    """change the implementation of used linked tuples 
    """
    def __init__(self):
        self._items = None
        self._size = 0

    def push(self, item):
        self._items = (item, self._items)
        self._size += 1
    
    def pop(self):
        (item, self._items) = self._items
        self._size -= 1
        return item 

    def __len__(self):
        return self._size

def test_Stack():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())
    print(s.pop())

    return

# dependency injection skill

# 7.17 Properties
# to intercept attribute access and handles it via user-defined methods
# a commone to use properties for implementing read-only computed data attributes  
#

# 7.18 Interfaces, and ABC  
# a common use of class typing relations is the specification of programming interfaces.
#   
# a base class(ABC) and a decoractor(@abstractmethods) are used together 
# to describe an interface (methods and properties for use in subclasses).
# 
# different classes would inherit from the base class and implement the required functionality.
# then base class might then be used for typing hinting or for defensive type enforcement via isinstancer()
import abc

class BasePizza(metaclass=abc.ABCMeta):
    default_ingredients = ['cheese']

    @classmethod  
    @abc.abstractmethod
    def get_ingredients(cls):  #an interface to be implemented by subclasses 
        """ Returns the ingredient list."""
        return cls.default_ingredients


class DietPizza(BasePizza):
    # use a subclass to extend the signature of the abstract method
    def get_ingredients(self, with_egg=False):
        egg = "egg" if with_egg else None
        # every Pizza also has access to the base class's default methanism for getting the ingredients list
        return [egg] + super().get_ingredients()

class Fridge():
    default_vegetables = "apple"

    def get_vegetables(self):
        return self.default_vegetables


class Pizza():
    def __init__(self, ingredients):
        self.ingredients = ingredients
    
    def get_ingredients(self):
        """Returns the ingredient list."""
        return self.ingredients

    #static methods belongs to the Pizza class
    # 1. Python does not have to instantiate a bound method
    # 2. the mthod does not depend on the state of the object
    @staticmethod
    def mix_ingredients(x, y):
        return x + y

    #class methods
    # the method is always bound to the class it is attached to
    # class methos are useful for creating factory methods
    # which instantiate objects using a different signature than __init__  
    @classmethod
    def from_fridge(cls, fridge):
        #a from_fridge() factory method
        return cls(fridge.get_vegetables())


def test_Pizza():
    p = Pizza("cheeze")
    print(Pizza.get_ingredients(p))
    # self argument is automatically set to Pizza instance
    # Note - we can access get_radius() from Pizza instance
    # Python will auto pass the object itself to the method's self parameter
    print(p.get_ingredients())

    # because static methods, we neednot bound method for each Pizza object
    print(Pizza.mix_ingredients("egg","cheese"))
    assert Pizza("cheeze").mix_ingredients is Pizza.mix_ingredients
    #
    print(DietPizza().get_ingredients())
    #
    # class method
    f = Fridge()
    # a brand-new Pizza with ingredients taken in  Fridge()
    new_pizza = Pizza.from_fridge(f)
    print(new_pizza.get_ingredients()) #apple


if __name__ == "__main__":
    #test_Account()
    #test_Stack()
    test_Pizza()
