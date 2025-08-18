def readout(file: str) -> list[list[str]]:
    '''
    This will simply readout the contents
    of a file into a 2d-array
    '''
    ret = []
    for line in open(file).read().splitlines():
        inner_ret = []
        for i in line:
            inner_ret.append(i)
        ret.append(inner_ret)
    return ret


def router(file: str | None = None, input: list[list[str]] | None = None,
           loop: bool = False) -> int | bool:
    '''
    Returns the number of unique squares a guard
    passes, following certain rules or wether
    or not she loops on a given map.

    >>> router("testMap.txt")
    41
    >>> router(input=readout("loopedMap.txt"), loop=True)
    True
    >>> router(input=readout("vartestMap.txt"), loop=True)
    False
    '''
    if not loop:
        map = readout(file)
    else:
        map = input
    pos_guard = [0, 0]
    for i in map:
        if "^" in i:
            for j in i:
                if j == "^":
                    break
                pos_guard[1] += 1
            break
        pos_guard[0] += 1
    rows, columns, direct, uniques, skip, looping = len(
        map), len(map[0]), "up", 0, True, False

    while skip:
        if loop and skip:
            looping = True

        while direct == "up" and pos_guard[0] >= 0 and skip:
            if pos_guard[0] - 1 >= 0 and\
                    map[pos_guard[0] - 1][pos_guard[1]] != "#" and\
                    skip:
                pos_guard[0] -= 1
                if map[pos_guard[0]][pos_guard[1]] != "X":
                    uniques += 1
                    map[pos_guard[0]][pos_guard[1]] = "X"
                    looping = False
            elif pos_guard[0] - 1 < 0:
                skip = False
            else:
                direct = "right"

        while direct == "right" and pos_guard[1] < columns and skip:
            if pos_guard[1] + 1 < columns and\
                    map[pos_guard[0]][pos_guard[1] + 1] != "#" and\
                    skip:
                pos_guard[1] += 1
                if map[pos_guard[0]][pos_guard[1]] != "X":
                    uniques += 1
                    map[pos_guard[0]][pos_guard[1]] = "X"
                    looping = False
            elif pos_guard[1] + 1 >= columns:
                skip = False
            else:
                direct = "down"

        while direct == "down" and pos_guard[0] < rows and skip:
            if pos_guard[0] + 1 < rows and\
                    map[pos_guard[0] + 1][pos_guard[1]] != "#" and\
                    skip:
                pos_guard[0] += 1
                if map[pos_guard[0]][pos_guard[1]] != "X":
                    uniques += 1
                    map[pos_guard[0]][pos_guard[1]] = "X"
                    looping = False
            elif pos_guard[0] + 1 >= rows:
                skip = False
            else:
                direct = "left"

        while direct == "left" and pos_guard[1] >= 0 and skip:
            if pos_guard[1] - 1 >= 0 and\
                    map[pos_guard[0]][pos_guard[1] - 1] != "#" and\
                    skip:
                pos_guard[1] -= 1
                if map[pos_guard[0]][pos_guard[1]] != "X":
                    uniques += 1
                    map[pos_guard[0]][pos_guard[1]] = "X"
                    looping = False
            elif pos_guard[1] - 1 < 0:
                skip = False
            else:
                direct = "up"
        if loop and looping:
            skip = False
    if loop:
        return looping
    return uniques


def obstructor(file: str) -> int:
    '''
    Checks all possible positions for the
    possibility of adding an obstacle
    and returns the number of positions
    that lead to a loop
    '''
    map = readout(file)
    loops, x, y = 0, 0, 0
    for i in map:
        for _ in i:
            if map[x][y] == ".":
                map[x][y] = "#"
                loops += router(input=copy(map), loop=True)
                map[x][y] = "."
            y += 1
        x += 1
        y = 0
    return loops


def printer(map: list[list[str]]) -> None:
    for line in map:
        print(line)


def copy(ele: list[list[str]]) -> list[list[str]]:
    new = []
    for i in ele:
        new_inner = []
        for j in i:
            new_inner.append(j)
        new.append(new_inner)
    return new


if __name__ == "__main__":
    print(obstructor("Map.txt"))
