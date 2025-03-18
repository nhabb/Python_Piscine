import pandas as p


def load(path: str) -> p.DataFrame:
    """This function loads a csv file and handles file errors"""
    try:
        fd = p.read_csv(path)
    except FileNotFoundError as e:
        print(e)
        exit(0)
    return (fd)
