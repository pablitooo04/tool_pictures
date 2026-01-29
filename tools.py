
from math import prod
import utils as utl
from copy import deepcopy
from math import prod


def saturator(data_input, multiplier: int) -> list:
    """
    Increases the saturation of the image by boosting the maximum color
    channel and reducing the minimum color channel for each pixel.

    Args:
        data_input (list): A list of tuples representing the RGB values of
        each pixel in the image.
    Returns:
        list: A list of tuples representing the modified RGB values of
        each pixel with increased saturation.
    """
    for px in range(len(data_input)):
        # load
        if px % ((len(data_input) // 1000) + 1) == 0:
            print("\r" + utl.gen_loading(px, len(data_input), 30, char='#'),
                  end="")
        # end_load

        index_max = data_input[px].index((max(data_input[px])))
        index_min = data_input[px].index((min(data_input[px])))
        new_color = list(data_input[px])
        new_color[index_max] = int(new_color[index_max] * 1.2**multiplier)
        new_color[index_min] = int(new_color[index_min] * 0.9**multiplier)
        new_color = [val if val <= 255 else 255 for val in new_color]
        data_input[px] = tuple(new_color)
    print()
    return data_input


def monochrome(data_input: list, color: tuple) -> list:
    """
    Converts the image to a monochrome version based on the specified color.
    Args:
        data_input (list): A list of tuples representing the RGB values of
        each pixel in the image.
        color (tuple): A tuple representing the RGB values of the desired
        monochrome color.
    Returns:
        list: A list of tuples representing the modified RGB values of
        each pixel in monochrome.
    """
    for px in range(len(data_input)):
        # load
        if px % ((len(data_input) // 1000) + 1) == 0:
            print("\r" + utl.gen_loading(px, len(data_input), 30, char='#'),
                  end="")
        # end_load
        current_color = data_input[px]
        new_color = [int(color[i] * (current_color[i] / 255))
                     for i in range(3)]
        new_color = tuple(new_color)
        data_input[px] = tuple(new_color)
    print()
    return data_input


def rescale(data_input: list, old_size: tuple, new_size: tuple) -> list:
    """
    Downscales the image to a new size using a nearest-neighbor approach.
    Args:
        data_input (list): A list of tuples representing the RGB values of
        each pixel in the image.
        old_size (tuple): A tuple representing the original size (width, height)
        of the image.
        new_size (tuple): A tuple representing the new size (width, height)
        of the image.
    Returns:
        list: A list of tuples representing the RGB values of each pixel
        in the downscaled image.
    """
    old_w, old_h = old_size
    new_w, new_h = new_size
    data = list(data_input)
    output = []
    ratio_x = old_w / new_w
    ratio_y = old_h / new_h

    for ny in range(new_h):
        sy = int(ny * ratio_y)
        for nx in range(new_w):
            sx = int(nx * ratio_x)
            index = sy * old_w + sx
            output.append(data[index])
            # load
            if (nx + new_w * ny) % 1000 == 0:
                print("\r" + utl.gen_loading((new_w*ny + nx), (new_h * new_w), 20, char='#'),
                      end="")
            # end_load

    print()

    return output


def blur(data_input: list, size: tuple) -> list:
    h, w = size
    total_px = h * w
    output = []

    kernel = [
        [1, 1, 1],
        [1, 0, 1],   # 0 au lieu de None
        [1, 1, 1]
    ]

    for px in range(total_px):
        color_px = [0, 0, 0]
        used_neighbors = 0

        neighbors = [
            (px - w - 1, kernel[0][0]), (px - w, kernel[0][1]), (px - w + 1, kernel[0][2]),
            (px - 1, kernel[1][0]),     (px,     kernel[1][1]), (px + 1, kernel[1][2]),
            (px + w - 1, kernel[2][0]), (px + w, kernel[2][1]), (px + w + 1, kernel[2][2])
        ]

        for idx, weight in neighbors:
            if weight == 0:
                continue
            if idx < 0 or idx >= total_px:
                continue
            # empêcher les sauts de ligne
            if abs(idx - px) == 1 and (idx // w) != (px // w):
                continue

            used_neighbors += 1
            for c in range(3):
                color_px[c] += data_input[idx][c] * weight

        # normalisation
        color_px = [round(c / used_neighbors) for c in color_px]

        output.append(tuple(color_px))

    return output

        






