def position(file: str) -> tuple[dict[str, list[tuple[int, int]]], int, int]:
    '''
    Translates the contents of a file into
    the coordinates of the different symbols
    '''
    cords = {}
    contents = open(file).read().splitlines()
    län = len(contents[0])
    for y in range(len(contents)):
        for x in range(län):
            if contents[y][x] != ".":
                if contents[y][x] not in cords:
                    cords[contents[y][x]] = [(x, y)]
                else:
                    cords[contents[y][x]] += [(x, y)]
    return (cords, län, len(contents))


def mirrorer(file: str) -> int:
    '''
    Finds the unique positions of the antennas mirrorings
    >>> mirrorer("testAntennas.txt")
    14
    '''
    antinodes = set()
    cords, xlen, ylen = position(file)
    for symbol in cords.values():
        while len(symbol) > 1:
            testval, symbol = symbol[0], symbol[1:]
            for cord in symbol:
                antinode1 = (2 * testval[0] - cord[0],
                             2 * testval[1] - cord[1])
                antinode2 = (2 * cord[0] - testval[0],
                             2 * cord[1] - testval[1])
                if antinode1[0] >= 0 and antinode1[1] >= 0 and antinode1[0] < xlen and antinode1[1] < ylen:
                    antinodes |= {antinode1}
                if antinode2[0] >= 0 and antinode2[1] >= 0 and antinode2[0] < xlen and antinode2[1] < ylen:
                    antinodes |= {antinode2}
    return len(antinodes)


def far_mirrorer(file: str) -> int:
    antinodes = set()
    cords, xlen, ylen = position(file)
    for symbol in cords.values():
        while len(symbol) > 1:
            testval, symbol = symbol[0], symbol[1:]
            for cord in symbol:
                leftlis, rightlis = [testval, cord], [cord, testval]
                m, n = 1, 1
                while True:
                    antinode = (
                        2 * leftlis[n][0] - leftlis[n - 1][0], 2 * leftlis[n][1] - leftlis[n - 1][1])
                    n += 1
                    if antinode[0] >= 0 and antinode[1] >= 0 and antinode[0] < xlen and antinode[1] < ylen:
                        leftlis.extend([tuple(antinode)])
                    else:
                        break
                while True:
                    antinode = (
                        2 * rightlis[m][0] - rightlis[m - 1][0], 2 * rightlis[m][1] - rightlis[m - 1][1])
                    m += 1
                    if antinode[0] >= 0 and antinode[1] >= 0 and antinode[0] < xlen and antinode[1] < ylen:
                        rightlis.extend([tuple(antinode)])
                    else:
                        break
                for i in leftlis:
                    antinodes |= {i}
                for i in rightlis:
                    antinodes |= {i}
    return len(antinodes)


print(far_mirrorer("Antennas.txt"))
