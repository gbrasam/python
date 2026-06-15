from PIL import Image, UnidentifiedImageError
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    load an image,
    convert it to RGB,
    print its shape,
    and return its pixels as a NumPy array
    """

    try:
        if not path:
            raise ValueError("empty path")

        with Image.open(path) as image:
            image = image.convert("RGB")
            pixels = np.array(image)

        return pixels

    except FileNotFoundError:
        print("Error: file not found")

    except UnidentifiedImageError:
        print("Error: corrupted or invalid image")

    except ValueError as error:
        print(f"AssertionError: {error}")

    return np.array([])
