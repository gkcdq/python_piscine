import sys


"""
(__doc__)

count_in_string() -> this function count and print
                     all different char in a string

__main__ -> check number of arguments
            call count_in_string()
"""


def count_in_string(s):
    upper = 0
    lower = 0
    punc = 0
    digit = 0
    space = 0
    all = 0

    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isdigit():
            digit += 1
        elif char.isspace():
            space += 1
        else:
            punc += 1
    all = upper + lower + digit + space + punc
    if (all == 0):
        print("Error: empty string.")
        return 1
    print("The text contains", all, "characters:")
    print(upper, "upper letters")
    print(lower, "lower letters")
    print(punc, "punctuation marks")
    print(space, "spaces")
    print(digit, "digits")


if __name__ == "__main__":
    if (len(sys.argv) > 2):
        print("AssertionError: provided only one argument.")
    else:
        count_in_string(sys.argv[1])
