import numpy as np


def check_params(family: list, start: int, end: int):
    """This function is responsible for the error handling"""
    if not (isinstance(family, list)):
        print("Family must be a list")
        exit(0)
    if not (isinstance(start, int)):
        print("Start is not an integer")
        exit(0)
    if not (isinstance(end, int)):
        print("End is not an integer")
        exit(0)
    rowLen = len(family[0])
    for fam in family:
        if not (isinstance(fam, list)):
            print("Family must be a list pf lists")
            exit(0)
        if not (len(fam) == rowLen):
            print("Rows do not have the same length")
            exit(0)


def slice_me(family: list, start: int, end: int) -> list:
    """This function slices the family list according to
    start and end values"""
    check_params(family, start, end)
    Array2D = np.array(family)
    print(f"My shape is: ({len(family)},{len(family[0])})")
    sliced = Array2D[start:end]
    print(f"My new shape is: ({len(sliced)},{len(sliced[0])})")
    return (sliced.tolist())
