import sys


def builiding():
    """This function allows us to count total charcters,
    uppercase,lowercase,punctuaution,spaces,digits"""
    dig = 0
    upp = 0
    space = 0
    lower = 0
    punct = 0
    punctuation_marks = '!"#$%&\'?()*+,-./'
    if len(sys.argv) > 2:
        raise AssertionError("Only one argument is allowed.")
    if len(sys.argv) == 1:
        text = input("What is the text count?\n")
        space += 1
    else:
        text = sys.argv[1]
    total = len(text)
    for char in text:
        if (char in punctuation_marks):
            punct += 1
        elif (char.isdigit()):
            dig += 1
        elif (char >= 'A' and char <= 'Z'):
            upp += 1
        elif (char >= 'a' and char <= 'z'):
            lower += 1
        elif (char == ' '):
            space += 1
    print(f"The text contains {total} letters")
    print(f"{upp} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuaution marks")
    print(f"{space} spaces")
    print(f"{dig} digits")


def main():
    """This is the main function"""
    builiding()


main()
