#
#ch9 - decorators and closures
# note: use for separating concerns and avoiding external unrelated logic "polluting"  
#       the core logic of the function or method  
#

def decorator(func):
    # manipulate func
    def inner():
        print('running inner()')
    return inner

# target = decorator(target)

#target() is decorated
@decorator
def target():
    print('running target()')
    return


def main():
    return

if __name__ == "__main__":
    target()
