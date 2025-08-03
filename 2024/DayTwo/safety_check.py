def reading(file: str) -> list[list[int]]:
    '''
    Divides a given file 'file' that has an arbitrary amount of
    lines with an arbitrary amount of numbers,
    each divided by space into a list of lists of numbers,
    with one inner list corresponding to one line of code

    >>> reading("testData.txt")
    [[7, 6, 4, 2, 1], [1, 2, 7, 8, 9], [9, 7, 6, 2, 1], [1, 3, 2, 4, 5], [8, 6, 4, 4, 1], [1, 3, 6, 7, 9]]
    '''

    invent = open(file).read().splitlines()
    ret = []
    for i in invent:
        ret.extend([[int(x) for x in i.split()]])
    return (ret)


def checking(file: str) -> int:
    '''
    This function checks how many reports in a given
    file are safe.
    A report is considered safe if it is:
    a) all increasing or decreasing and
    b) doing no jumps bigger than 3 and of at least 1

    >>> checking("testData.txt")
    2
    >>> checking("ownData.txt")
    0
    '''

    data = reading(file)
    safe = 0
    for line in data:
        remember = -1
        sizing = None
        for number in line:
            if remember == -1:
                remember = number
                continue
            elif remember < number and sizing is True:
                break
            elif remember > number and sizing is False:
                break
            elif remember < number:
                sizing = False
            elif remember > number:
                sizing = True
            if abs(remember - number) < 1 or abs(remember - number) > 3:
                break
            remember = number
        else:
            safe += 1
    return safe


def dampener(file: str) -> int:
    '''
    Does the same as 'checking' but may remove one level
    if the solution is safe afterwards

    >>> dampener("testData.txt")
    4
    >>> dampener("ownData.txt")
    6
    '''

    data = reading(file)
    safe = 0
    for line in data:
        error = False
        län = len(line) - 1
        if line[0] < line[län] and line[0] < line[län - 1] \
                or line[1] < line[län] and line[1] < line[län - 1]:
            direction = True
        else:
            direction = False
        if rule_check(line[0], line[1], direction) or \
                rule_check(line[0], line[2], direction):
            rem, bak = line[0], line[0]
        elif rule_check(line[1], line[2], direction):
            rem = line[1]
        else:
            continue

# ___________________________________________________________ #

        for num in line[1:]:
            if rule_check(rem, num, direction):
                bak = rem
                rem = num
            elif rule_check(bak, num, direction) and \
                    not error:
                error = True
                rem = num
            elif error:
                break
            else:
                error = True
        else:
            safe += 1
    return safe


def rule_check(last_number: int, next_number: int, direction: bool) -> bool:
    '''
    checks wether or not two numbers adhede to the ruleset.
    In direction is 'True' corresponding to growing and
    'False' corresponding to shrinking.

    >>> rule_check(3, 7, True)
    False
    >>> rule_check(4, 5, True)
    True
    >>> rule_check(9, 5, True)
    False
    '''

    if last_number < next_number and not direction:
        return False
    elif last_number > next_number and direction:
        return False
    elif abs(last_number - next_number) > 3 or \
            abs(last_number - next_number) < 1:
        return False
    return True


if __name__ == "__main__":
    print(dampener("Data.txt"))
