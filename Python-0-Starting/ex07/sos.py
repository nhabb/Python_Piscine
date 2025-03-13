import sys


def main():
    """This program transforms letters and numbers into morse code"""
    morse = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ".",
        "F": "..-.. ",
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
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. "}
    if (len(sys.argv) != 2):
        print("AssertionError: The arguments are bad")
        return
    res = ""
    for char in sys.argv[1]:
        if (char == '$'):
            print("Input is not a leter or number")
            exit(1)
    for char in sys.argv[1].upper():
        if (char not in morse):
            print("Input is not a leter or number")
            return
        res += morse[char]
    print(res.strip())


main()
