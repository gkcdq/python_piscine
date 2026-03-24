import sys


def modulo(n):
    if (n % 2 == 0):
        print("I'm Even.")
    else:
        print("I'm Odd.")
    return 0


if (len(sys.argv) != 2):
    print("AssertionError: provide exactly one argument.")
else:
    try:
        modulo(int(sys.argv[1]))
    except ValueError:
        print("AssertionError: argument is not an integer.")