import sys
from ft_filter import ft_filter


def random(n):
    if (n % 2 == 0):
        return True
    else:
        return False


number = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def check_line(words):
    


if __name__ == "__main__":
    if (len(sys.argv) != 3):
        print("AssertionError: provid 2 arguments <list of words> <length>")
    if (sys.argv[1].isdigit()):
        print("AssertionError: first argument need to be a <list of words>")
    if (sys.argv[2].isdigit()):
        {}
    else:
        print("AssertionError: second argument need to be a <length>")
    words = sys.argv[1].split()
    if (len(words) <= 1):
        print("AssertionError: first argument need to be a <list of words>")
    if (check_line(words) == 0):
        ft_filter(words, )
        