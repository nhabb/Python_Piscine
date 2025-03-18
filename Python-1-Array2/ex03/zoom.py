import numpy as np
import matplotlib.pyplot as mat
from load_image import ft_load


def zoom_image(image: np.array):
    """This function zooms the image and chamges its color to gray"""
    if isinstance(image, str):
        print(image)
        return
    print(f"The shape of image is: {image.shape}")
    print(image)
    square = image[100:500, 450:850, :1]
    square1 = square.squeeze()
    print(f"New shape after slicing: {square.shape} or {square1.shape}")
    print(square)
    mat.imshow(square, cmap="gray")
    mat.show()


def main():
    """Main function"""
    image = ft_load("animal.jpeg")
    zoom_image(image)


main()
