import utils as utl
import tools
from sys import argv
from PIL import Image

usage = "python3 main.py <image_name> --effect"
usage_monochrome = "--monochrome <r> <g> <b>"
filename_exemple = "picture.png, picture.jpg"
flags = {"--sature", "--monochrome"}

def save_img(data: list, size: tuple, file_name: str) -> None:
    output_img = Image.new("RGB", size)
    output_img.putdata(data)
    output_img.save(f"output/{file_name}")

def select(offset: int, argv: list, file_name: str, data_input: list) -> tuple:
    
    print(argv[i])
    if argv[i] == "--sature":
        data_output = tools.saturator(list(data_input))
        return (0, data_output)
    elif argv[i] == "--monochrome":
        try:
            color = tuple(int(argv[c]) for c in range(offset + 1, offset + 4))
        except ValueError:
            raise ValueError(usage_monochrome)
        if not all(0 <= value <= 255 for value in color):
            raise ValueError(usage_monochrome)
        data_output = tools.monochrome(list(data_input), color)
        return (3, data_output)
    else:
        raise ValueError("flag pas bon")

if __name__ == "__main__":
    input_img = Image.open("img/" + argv[1]).convert("RGB")
    argc = len(argv)
    data = input_img.getdata()

    if argc < 3:
        raise ValueError(usage)
    elif not utl.filename_is_valid(argv[1]):
        raise ValueError("file_name must be like ", filename_exemple)
    i = 2
    while(i < len(argv)):
        offset, data = select(i, argv, argv[1], data)
        i += offset + 1
        if i == len(argv):
            save_img(data, input_img.size, argv[1])