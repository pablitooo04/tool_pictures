import utils as utl
import tools
from sys import argv
from PIL import Image

usage = "python3 main.py <image_name> --effect"
usage_monochrome = "--monochrome <r> <g> <b>"
usage_downscale = "--downscale <x> <y>"
filename_exemple = "picture.png, picture.jpg"
flags = {"--sature", "--monochrome", "--downscale"}

def save_img(data: list, size: tuple, file_name: str) -> None:
    """
    Saves the modified image data to a new image file.
    Args:
        data (list): A list of tuples representing the RGB values of
        each pixel in the modified image.
        size (tuple): A tuple representing the size (width, height) of
        the image.
        file_name (str): The name of the output image file.
    Returns:
        None
    """
    output_img = Image.new("RGB", size)
    output_img.putdata(data)
    output_img.save(f"output/{file_name}")

def select(offset: int, argv: list, file_name: str,
           data_input: list, size: int) -> tuple:
    """
    Selects and applies the appropriate image effect based on the command-line
    arguments.
    Args:
        offset (int): The current index in the command-line arguments.
        argv (list): The list of command-line arguments.
        file_name (str): The name of the input image file.
        data_input (list): A list of tuples representing the RGB values of
        each pixel in the image.
        size (tuple): A tuple representing the size (width, height) of
        the image.
    Returns:
        tuple: A tuple containing the number of additional arguments consumed,
        the modified image data, and the new size of the image.
    """
    print(f"[{argv[i][2:]}]".upper())

    if argv[i] == "--sature":
        data_output = tools.saturator(list(data_input))
        return (0, data_output, size)

    elif argv[i] == "--monochrome":
        try:
            color = tuple(int(argv[c]) for c in range(offset + 1, offset + 4))
        except (ValueError, IndexError):
            print(usage_monochrome)
            exit(1)
        if not all(0 <= value <= 255 for value in color):
            print(usage_monochrome)
            exit(1)
        data_output = tools.monochrome(list(data_input), color)
        return (3, data_output, size)

    elif argv[i] == "--downscale":
        try:
            new_size = tuple(int(argv[c])
                             for c in range(offset + 1, offset + 3))
        except (ValueError, IndexError):
            raise ValueError(usage_downscale)
        if not all(0 <= new_size[i] <= size[i] for i in range(2)):
            raise ValueError(usage_monochrome + "trop grand")
        data_output = tools.downscale(data_input, size, new_size)
        return (2, data_output, new_size)

    else:
        raise ValueError("flag pas bon")

if __name__ == "__main__":
    input_img = Image.open("img/" + argv[1]).convert("RGB")
    argc = len(argv)
    data = input_img.getdata()
    size = input_img.size

    if argc < 3:
        raise ValueError(usage)
    elif not utl.filename_is_valid(argv[1]):
        raise ValueError("file_name must be like ", filename_exemple)
    i = 2
    while (i < len(argv)):
        offset, data, size = select(i, argv, argv[1], data, size)
        i += offset + 1
        if i == len(argv):
            save_img(data, size, argv[1])
