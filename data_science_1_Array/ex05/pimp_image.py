import numpy as np
import matplotlib.pyplot as plt


def display(
    array: np.ndarray,
    title: str,
    cmap: str | None = None
) -> None:
    """display an image with a title"""

    plt.imshow(array, cmap=cmap)
    plt.title(title)
    plt.show()


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    invert the colors of an RGB image while preserving its shape

    allowed operators: =, +, -, *
    """

    negative_image = 255 - array

    display(negative_image, "Negative Image")

    return negative_image


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    keep the red channel and remove the others
    while preserving the image shape

    allowed operators: =, *
    """

    red_image = array.copy()
    red_image[:, :, 1] *= 0
    red_image[:, :, 2] *= 0

    display(red_image, "Red Image")

    return red_image


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    keep the green channel and remove the others
    while preserving the image shape

    allowed operators: =, -
    """

    green_image = array.copy()
    green_image[:, :, 0] -= green_image[:, :, 0]
    green_image[:, :, 2] -= green_image[:, :, 2]

    display(green_image, "Green Image")

    return green_image


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    keep the blue channel and remove the others
    while preserving the image shape.

    allowed operators: =
    """

    blue_image = array.copy()
    blue_image[:, :, 0] = 0
    blue_image[:, :, 1] = 0

    display(blue_image, "Blue Image")

    return blue_image


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    convert an RGB image to grayscale
    while preserving the image shape

    allowed operators: =, /
    """

    grey_image = array.copy()
    grey_image[:, :, 2] = grey_image[:, :, 2] / 3
    grey_image[:, :, 0] = grey_image[:, :, 2]
    grey_image[:, :, 1] = grey_image[:, :, 2]

    display(grey_image, "Grey Image", cmap="gray")

    return grey_image
