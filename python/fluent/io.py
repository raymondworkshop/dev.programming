
import argparse

def main(argv):
    p = argparse.ArgumentParser()

    args = p.parse_args(args=argv)

    #data representation
    a = b'hello'
    _a = a.decode('utf-8')
    print(_a)
    b = 'hello'
    _b = b.encode('utf-8')
    print(_b)

    #


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])