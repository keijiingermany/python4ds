import numpy as np
from PIL import Image


def ft_invert(array) -> np.ndarray:
    """
    Inverts the color of the image received.
    Allowed operators: =, +, -, *
    """
    inverted = 255 - array

    img = Image.fromarray(inverted.astype(np.uint8))
    img.show()

    return inverted


def ft_red(array) -> np.ndarray:
    """
    Applies a red filter to the image.
    Allowed operators: =, *
    """
    red = array.copy()
    red[:, :, 1] = red[:, :, 1] * 0
    red[:, :, 2] = red[:, :, 2] * 0

    img = Image.fromarray(red.astype(np.uint8))
    img.show()

    return red


def ft_green(array) -> np.ndarray:
    """
    Applies a green filter to the image.
    Allowed operators: =, -
    """
    green = array.copy()
    green[:, :, 0] = green[:, :, 0] - green[:, :, 0]
    green[:, :, 2] = green[:, :, 2] - green[:, :, 2]

    img = Image.fromarray(green.astype(np.uint8))
    img.show()

    return green


def ft_blue(array) -> np.ndarray:
    """
    Applies a blue filter to the image.
    Allowed operators: =
    """
    blue = array.copy()
    blue[:, :, 0] = 0
    blue[:, :, 1] = 0

    img = Image.fromarray(blue.astype(np.uint8))
    img.show()

    return blue


def ft_grey(array) -> np.ndarray:
    """
    Converts the image to grayscale.
    Allowed operators: =, /
    """
    grey = array.copy()
    # Calculate average of RGB channels using division
    avg = (grey[:, :, 0] / 3) + (grey[:, :, 1] / 3) + (grey[:, :, 2] / 3)
    grey[:, :, 0] = avg
    grey[:, :, 1] = avg
    grey[:, :, 2] = avg

    img = Image.fromarray(grey.astype(np.uint8))
    img.show()

    return grey


def main():
    """
    Main function for testing.
    """
    from load_image import ft_load

    array = ft_load("../landscape.jpg")
    if array is None:
        return

    ft_invert(array)
    ft_red(array)
    ft_green(array)
    ft_blue(array)
    ft_grey(array)


if __name__ == "__main__":
    main()
