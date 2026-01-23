def filename_is_valid(file_name: str) -> bool:
    if ".png" not in file_name and ".jpg" not in file_name:
        return False
    elif file_name == ".png" or file_name == ".jpg":
        return False
    else:
        return True
    
def gen_loading(current: int, end: int, size=20, char='#') -> tuple:
    assert(len(char))
    p = (current/end) * 100 + 1
    n = int(p / 100 * size) + 1
    bar = '['
    bar += "".join([char for i in range(n)])
    bar += "".join(["." for i in range(size - n)])
    bar += "] " + str(int(p)) + "%"
    return bar
    

