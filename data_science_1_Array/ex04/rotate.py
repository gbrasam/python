from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def zoom(image: np.ndarray) -> np.ndarray:
    """
    apply a centered zoom using slicing,
    keep a single channel of the cropped image,
    """

    # unpacking image
    h, w = image.shape[:2]

    # setting image final size
    zh, zw = 400, 400

    # zoom / slicing
    start_h = (h - zh) // 2
    end_h = start_h + zh
    start_w = (w - zw) // 2
    end_w = start_w + zw
    cropped = image[start_h:end_h, start_w:end_w]

    # keep only one channel while preserving the channel dimension
    zoom_gray = cropped[:, :, 0:1]

    return zoom_gray


def transpose(image: np.ndarray) -> np.ndarray:
    """
    transpose an image by swapping its rows and columns

    args:
        image: A NumPy array representing the image

    returns:
        The transposed image as a NumPy array
    """

    rows, cols = image.shape
    transposed = np.zeros((cols, rows), dtype=image.dtype)
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = image[i][j]

    return transposed


def main():
    """
    load an image, apply a centered zoom,
    keep a single channel, transpose the image,
    print its shape and display the result
    """

    # load an image
    image = ft_load("animal.jpeg")
    if image.size == 0:
        return

    # apply centered zoom
    zoom_gray = zoom(image)
    print(f"The shape of image is: {zoom_gray.shape}")
    print(zoom_gray)

    # transpose image
    transposed = transpose(zoom_gray[:, :, 0])
    print(f"New shape after Transpose: {transposed.shape}")
    print(transposed)

    # display the transposed image in grayscale
    plt.imshow(transposed, cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()
