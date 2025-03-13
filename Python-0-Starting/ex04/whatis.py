import sys

def isEven(value):
    if value % 2 == 0:
        print(f"{value} is even")
    else:
        print(f"{value} is odd")

def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError("Error: Exactly one argument is required.")
        value = sys.argv[1].strip()
        value = int(value)
        isEven(value)
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except ValueError:
        print("Error: Argument is not a valid integer.")

main()