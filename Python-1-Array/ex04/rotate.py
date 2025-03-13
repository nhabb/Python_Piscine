import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def custom_transpose(image: np.array):
    """Manually transposes a 3D NumPy image array
    (height, width, channels) and fixes orientation."""
    h, w, c = image.shape
    transposed = np.zeros((w, h, c), dtype=image.dtype)
    for i in range(h):
        for j in range(w):
            transposed[j, i] = image[i, j]
    return transposed[::-1]


def rotate_image(image: np.array):
    """Cuts the image,changes its color and displays the modified image"""
    if isinstance(image, str):
        print(image)
        return
    square = image[100:500, 450:850, :1]
    square1 = square.squeeze()
    print(f"The shape of image is: {square.shape} or {square1.shape}")
    print(square)
    transposed_square = custom_transpose(square)
    transposed_square1 = transposed_square.squeeze()
    plt.imshow(transposed_square, cmap="gray")
    plt.show()
    print(f"New Shape after Transpose: {transposed_square1.shape}")
    print(transposed_square)


def main():
    """Main function"""
    image = ft_load("animal.jpeg")
    rotate_image(image)


main()
