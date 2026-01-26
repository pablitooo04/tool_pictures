import utils as utl


def saturator(data_input) -> list:
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
        new_color[index_max] = int(new_color[index_max] * 1.2)
        new_color[index_min] = int(new_color[index_min] * 0.9)
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


def cursed_downscale(data_input: list, new_size: tuple) -> list:
    """
    Downscales the image to a new size by sampling pixels at regular intervals.
    Args:
        data_input (list): A list of tuples representing the RGB values of
        each pixel in the image.
        new_size (tuple): A tuple representing the desired width and height
        of the downscaled image.
    Returns:
        list: A list of tuples representing the RGB values of each pixel in
        the downscaled image.
    """
    new_total_pixel = new_size[0] * new_size[1]
    data_output = []
    for px in range(len(data_input)):
        # load
        if px % ((len(data_input) // 1000) + 1) == 0:
            print("\r" + utl.gen_loading(px, len(data_input), 30, char='#'),
                  end="")
        # end_load
        if px % (round(len(data_input)/new_total_pixel)) == 0:
            data_output.append(data_input[px])

    while len(data_output) != new_total_pixel:
        if len(data_output) > new_total_pixel:
            data_output.pop()
        else:
            data_output.append((0, 0, 0))
    print()
    return data_output
