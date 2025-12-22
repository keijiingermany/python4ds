from PIL import Image
import numpy as np


def ft_load(path: str):
    """
    Load an image from the given path and return it as NumPy array in RGB.
    Prints the shape of the image.
    """
    try:
        if not isinstance(path, str):
            print("Error: Path must be a string.")
            return None

        if not path.lower().endswith((".jpg", ".jpeg")):
            print("Error: Only JPG and JPEG formats are supported.")
            return None

        image = Image.open(path)
        image = image.convert("RGB")
        array = np.asarray(image)

        print(f"The shape of image is: {array.shape}")
        return array

    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return None
    except Exception as error:
        print(f"Error: {error}")
        return None


def main():
    """
    Main function for manual testing.
    """
    ft_load("../landscape.jpg")
    ft_load("../animal.jpeg")


if __name__ == "__main__":
    main()
