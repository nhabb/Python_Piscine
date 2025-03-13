def NULL_not_found(object: any) -> int:
    if (object == None):
        print(f"Nothing : None {object.__class__}")
    elif (object != object):
        print(f"Cheese : Nan {object.__class__}")
    elif (object is False):
        print(f"Fake : False {object.__class__}")
    elif (object == 0):
        print(f"Zero : 0 {object.__class__}")
    elif (object == ""):
        print(f"Empty : {object.__class__}")
        return (0)
    else:
        print("Type not found")
    return (1)