import numpy as np

from PIL import Image


def random_noise_image(width, height):
    random_image = Image.fromarray(
        np.random.randint(0, 255, (width, height, 3), dtype=np.dtype('uint8'))
    )
    return random_image


def gradient_2d(start, stop, width, height, is_horizontal):
    if is_horizontal:
        return np.tile(np.linspace(start, stop, width), (height, 1))
    else:
        return np.tile(np.linspace(start, stop, height), (width, 1)).T


def gradient_3d(width, height, starts, stops, is_horizontal_list):
    result = np.zeros((height, width, len(starts)), dtype=float)

    for i, (start, stop, is_horizontal) in enumerate(zip(starts, stops, is_horizontal_list)):
        result[:, :, i] = gradient_2d(start, stop, width, height, is_horizontal)

    return result


def random_gradient_image(width, height):
    array = gradient_3d(
        width,
        height,
        (0, 0, np.random.randint(0, 255)),
        (np.random.randint(1, 255), np.random.randint(2, 255), np.random.randint(3, 128)),
        (True, False, False)
    )
    random_image = Image.fromarray(np.uint8(array))
    return random_image
