from load_image import ft_load
import matplotlib.pyplot as plt


def main():
    """
    load an image,
    apply a centered zoom using slicing,
    keep a single channel of the cropped image,
    print the new shape,
    and display the result using a grayscale colormap.
    """

    image = ft_load("animal.jpeg")
    if image.size == 0:
        return
    print(image)

    # unpacking image
    h, w = image.shape[:2]
    # setting image final size
    zh, zw = 400, 400
    # zoom / slicing
    start_h = (h - zh) // 2
    end_h = start_h + zh
    start_w = (w - zw) // 2
    end_w = start_w + zw
    zoom = image[start_h:end_h, start_w:end_w]
    # keep only one channel while preserving the channel dimension
    zoom_gray = zoom[:, :, 0:1]
    # print new shape
    print(f"New shape after slicing: {zoom_gray.shape}")
    print(zoom_gray)
    # zoom_gray[:, :, 0] matplotlib expects a 2D array for grayscale display.
    plt.imshow(zoom_gray[:, :, 0], cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()
