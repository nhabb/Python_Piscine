import pandas as p


def load(path: str) -> p.DataFrame:
    """This function loads a csv file and handles file errors"""
    try:
        fd = p.read_csv(path)
        dim = fd.shape
        print(f"Loading dataset of dimensions {dim}")
    except Exception as e:
        print(e)
        exit(0)
    return (fd)
