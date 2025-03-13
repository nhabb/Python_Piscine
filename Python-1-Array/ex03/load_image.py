from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    """This function loads the image and handles the file errors"""
    try:
        img = Image.open(path)
        if not path.endswith(('.jpg', '.jpeg')):
            raise AssertionError
    except AssertionError:
        return "Erorr: Image format must be JPEG or JPG"
    except FileNotFoundError:
        return f"Error: {path} does not exist."
    img_rgb = img.convert('RGB')
    img_array = np.array(img_rgb)
    return img_array
