#
#ch9 - decorators and closures
#

def deco(func):
    def inner():
        print('running inner()')
    return inner

@deco
def target():
    print('running target()')
    return


def main():
    return

if __name__ == "__main__":
    target()
