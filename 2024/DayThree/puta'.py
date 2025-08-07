def optimized_readout(file: str, readout: bool = True) -> list[str]:
    '''
    Reads out a file or, alternativly if readout is False,
    optimizes a sttring, returning only the
    parts following an m.
    The length of the returned strings is between
    seven and eleven for the max and min length of a 'mul'
    command are inbetween that range.
    '''
    if readout:
        data_string = open(file).read().split("m")
    else:
        data_string = file.split("m")
    optimized_data = []
    for i in data_string:
        if len(i) >= 7:
            optimized_data.append(i[:11])
    return optimized_data


def readout_prep(file: str) -> str:
    '''
    Prepares a given file by cutting out the parts
    inbetween a 'do()' and 'don't()' statement
    '''
    data_string = open(file).read().split("d")
    optimized_data = data_string[0]
    for i in data_string[1:]:
        if i[:3] == "o()":
            optimized_data += i
    return optimized_data


def mult(file: str, extra: bool = False) -> int:
    '''
    Reads out a given file and multiplies x and y
    for each 'mul(x,y)' in the file.
    If there is any character obstructing the
    'mul' command it gets ignored.
    The numbers get added up which is the return-value.
    If extra is True, it will also filter out
    parts behind 'don't()' statements

    >>> mult("testInput.txt")
    161
    >>> mult("lattertestInput.txt", True)
    48
    '''
    if extra:
        commands = optimized_readout(readout_prep(file), False)
    else:
        commands = optimized_readout(file)
    result = 0
    for comand in commands:
        if comand[:3] == "ul(":
            mul1, mul2, latter, count = "0", "0", False, 0
            for num in comand[3:]:
                if num.isdecimal() and latter and count < 3:
                    mul2 += num
                    count += 1
                elif num.isdecimal() and count < 3:
                    mul1 += num
                    count += 1
                elif num == "," and count > 0 and count < 4:
                    count, latter = 0, True
                elif num == ")" and count > 0 and count < 4:
                    result += int(mul1) * int(mul2)
                    break
                else:
                    break
    return result


if __name__ == "__main__":
    print(mult("Input.txt", True))
