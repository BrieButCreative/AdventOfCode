from Control import splicer


# I will most definitly add comments
# (like ill do my best but im lowkey dysfunctional,
# so yeah... no promises...
# BUT ILL GIVE IT MY BEST!)


def order(file: str) -> int:
    '''
    The pinicle of the prior Program;
    Corrects the ordering in the misordered
    command lines and gives back their value
    via controller()

    >>> order("testOrdering.txt")
    123
    '''
    (restrictions, programs) = splicer(file)
    corrected_programs_middle = 0
    for command in programs:
        buffer, copy, län = [], [], len(command)
        for val in command:
            for i in restrictions.get(val, []):
                double = check(i, copy, buffer,
                               command, restrictions)
                if double[0]:
                    copy, buffer = double[1]
                    continue
                buffer.append(val)
                break
            else:
                copy.append(val)

        while buffer != []:
            for j in buffer:
                for i in restrictions.get(j, []):
                    double = check(i, copy, buffer,
                                   command, restrictions)
                    if double[0]:
                        copy, buffer = double[1]
                        continue
                    break
                else:
                    copy.append(j)
                    buffer.remove(j)

        if copy != command:
            corrected_programs_middle += copy[län // 2]
    return (corrected_programs_middle)


def check(tester: int, past_com: list[int | None],
          overflow: list[int | None],
          com: list[int], dependencies: dict[int,
          list[int]]) -> tuple[bool, tuple[list[int], list[int]] | None]:
    '''
    Passes back a big argument!
    It checks wether or not theres an 'Error'
    with the given value and, if so,
    finds out if the buffer values can be used to clear
    it up.
    '''
    if tester not in past_com and tester in com:
        if tester in overflow:
            for i in dependencies.get(tester, []):
                double = check(i, past_com, overflow,
                               com, dependencies)
                if double[0]:
                    past_com, overflow = double[1]
                    continue
                break
            else:
                past_com.append(tester)
                overflow.remove(tester)
                return (True, (past_com, overflow))
        return (False, None)
    else:
        return (True, (past_com, overflow))


if __name__ == "__main__":
    print(order("Ordering.txt"))
