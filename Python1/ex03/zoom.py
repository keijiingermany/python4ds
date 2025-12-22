from PIL import Image
from load_image import ft_load


def main():
    """
    Main function for zooming the image.
    """
    try:
        array = ft_load("../animal.jpeg")
        if array is None:
            return

        print(array)

        sliced = array[100:500, 450:850]

        grey = sliced[:, :, 0:1]

        print(f"New shape after slicing: {grey.shape}")
        print(grey)

        # Display the zoomed image using PIL
        img = Image.fromarray(grey[:, :, 0], mode='L')
        img.show()

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
