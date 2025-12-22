import numpy as np
from PIL import Image
from load_image import ft_load


def ft_transpose(array: np.ndarray) -> np.ndarray:
    """
    Manually transpose a 2D array without using library functions.

    Args:
        array: 2D numpy array to transpose

    Returns:
        Transposed array
    """
    rows, cols = array.shape
    transposed = np.zeros((cols, rows), dtype=array.dtype)

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = array[i][j]

    return transposed


def main():
    """
    Main function for rotating the image.
    """
    try:
        array = ft_load("../animal.jpeg")
        if array is None:
            return

        sliced = array[100:500, 450:850]

        grey = sliced[:, :, 0]

        print(f"The shape of image is: {grey.shape}")
        print(grey)

        transposed = ft_transpose(grey)

        print(f"New shape after Transpose: {transposed.shape}")
        print(transposed)

        img = Image.fromarray(transposed, mode='L')
        img.show()

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
