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


def test():
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
class Stack(list):
    ...


if __name__ == "__main__":
    test()