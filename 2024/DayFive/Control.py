def splicer(file: str) -> tuple[dict[int, int], list[list[int]]]:
    '''
    Splits a given files content into a tuple,
    containing a dictionary with the pairs of restrictions
    and a list of the list of the commands.
    '''

    contents = open(file).read().splitlines()
    left, right = 0, len(contents) - 1
    while True:
        middle = (left + right) // 2
        if "" == contents[middle]:
            break
        elif "|" in contents[middle]:
            left = middle + 1
        else:
            right = middle - 1
    restrictions, operations = contents[:middle], contents[middle + 1:]
    final_operations = []
    for i in operations:
        final_operations.append([int(num) for num in i.split(",")])
    restrict_dic = redic(restrictions)
    return restrict_dic, final_operations


def redic(restrictions: list[str]) -> dict[int, int]:
    '''
    Turns a given list into adictionary with the
    given restraints
    '''
    restrictions = sorted(restrictions, key=lambda x: x.split("|")[1])
    retdic = {}
    for res in restrictions:
        val = [int(x) for x in res.split("|")]
        if val[1] in retdic.keys():
            retdic[val[1]] += [val[0]]
        else:
            retdic |= {val[1]: [val[0]]}
    return retdic


def controller(file: str) -> int:
    '''
    Checks how many 'pages' at the end of the file
    are in the right order.
    Returns the sum of the middle values of these.

    >>> controller("testOrdering.txt")
    143
    '''
    temp, sums = splicer(file), 0
    orders, pages = temp[0], temp[1]
    for lists in pages:
        copy = []
        for val in lists:
            for i in orders.get(val, []):
                if i not in copy and i in lists:
                    break
            else:
                copy.append(val)
                continue
            break
        if copy == lists:
            sums += lists[len(lists) // 2]
    return sums


if __name__ == "__main__":
    print(controller("Ordering.txt"))
