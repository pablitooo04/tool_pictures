from PIL import Image

def filename_is_valid(file_name: str) -> bool:
    if ".png" not in file_name and ".jpg" not in file_name:
        return False
    elif file_name == ".png" or file_name == ".jpg":
        return False
    else:
        return True


def gen_loading(current: int, end: int, size=20, char='#') -> tuple:
    assert (len(char))
    p = (current/end) * 100 + 1
    n = round(p / 100 * size) + 1
    bar = '['
    bar += "".join([char for i in range(n)])
    bar += "".join(["." for i in range(size - n)])
    bar += "] " + str(int(p)) + "%"
    return bar

def get_stats(img: Image, img_name: str) -> None:
    print("[IMG STATS]\n")
    print(f"NAME:\t{img_name}")
    print(f"SIZE:\t{img.size[0]}x{img.size[1]}")
    print(f"FORMAT:\t{img_name[img_name.rindex('.')+1:]}")
    print(f"MODE:\t{img.mode}")