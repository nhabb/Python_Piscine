import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[float]:
    """This fnction calculates BMI"""
    if not (isinstance(height, list) and isinstance(weight, list)):
        print("Height and weight should both be a list")
        exit(0)
    if not (len(height) == len(weight)):
        print("Weight and height should have the same list")
        exit(0)
    for h in height:
        if not (isinstance(h, int) or isinstance(h, float)):
            print("Height must be int or float")
            exit(0)
        if not (h > 0):
            print("Height should be a positive value")
            exit(0)
    for w in weight:
        if not (isinstance(w, int) or isinstance(h, float)):
            print("Weight must be int or float")
            exit(0)
        if not (w > 0):
            print("Weight should be a positive value")
            exit(0)
    return list(np.array(weight) / (np.array(height) ** 2))


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """This function compares the list of BMI's with the limit"""
    if not (isinstance(bmi, list) or isinstance(limit, (int, float))):
        print("bmi should be a list and limit should be an int or float")
        exit(0)
    for b in bmi:
        if (not isinstance(b, (int, float)) or b <= 0):
            print("All BMI values must be positive")
            exit(0)
    if (limit < 0):
        print("Limit must be positive")
        exit(0)
    lim = []
    for b in bmi:
        lim.append(b > limit)
    return lim
