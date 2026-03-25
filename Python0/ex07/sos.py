import sys


NESTED_MORSE = {" ": "/ ",
                "A": ".- ",
                "B": "-... ",
                "C": "-.-. ",
                "D": "-.. ",
                "E": ". ",
                "F": "..-. ",
                "G": "--. ",
                "H": ".... ",
                "I": ".. ",
                "J": ".--- ",
                "K": "-.- ",
                "L": ".-.. ",
                "M": "-- ",
                "N": "-. ",
                "O": "--- ",
                "P": ".--. ",
                "Q": "--.- ",
                "R": ".-. ",
                "S": "... ",
                "T": "- ",
                "U": "..- ",
                "V": "...- ",
                "W": ".-- ",
                "X": "-..- ",
                "Y": "-.-- ",
                "Z": "--.. ",
                "1": ".---- ",
                "2": "..--- ",
                "3": "...-- ",
                "4": "....- ",
                "5": "..... ",
                "6": "-.... ",
                "7": "--... ",
                "8": "---.. ",
                "9": "----. ",
                "0": "----- "
                }


if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("AssertionError: the argument are bad")
        sys.exit(1)
    string = sys.argv[1].upper()
    morse = ""
    for char in string:
        if char in NESTED_MORSE:
            morse += NESTED_MORSE[char]
        else:
            print("AssertionError: the argument are bad")
            sys.exit(1)
    print(morse)
