import sys
from ft_filter import ft_filter


if __name__ == "__main__":
    if (len(sys.argv) != 3):
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    elif (sys.argv[1].isdigit()):
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    elif (sys.argv[2].isdigit()):
        {}
    else:
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    words = sys.argv[1].split()
    if (len(words) <= 1):
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    result = ft_filter(lambda w: len(w) > int(sys.argv[2]), words)
    print(list(result))
