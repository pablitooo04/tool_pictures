import utils as utl


def saturator(data_input) -> list:
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
