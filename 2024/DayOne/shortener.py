def sortdis(file: str) -> str:
    '''
    Ermittelt aus dem Inhalt der gegebenen Datei
    wie weit die jeweils kleinsten Werte auseinander liegen.

    >>> sortdis("test_locations.txt")
    "11"
    '''

    # We first read out the first to culumns
    # and save them as lists
    leftlis, rightlis = [], []
    with open(file) as page:
        for line in page:
            left, right = line.split(" ", 1)
            left = left.strip()
            right = right.strip(" \n")
            leftlis.append(left)
            rightlis.append(right)

# #############We#then#sort#these#lists################# #

    rightlis, leftlis = sorted(rightlis), sorted(leftlis)
    n = len(rightlis)
    sum = 0

    # Finally we go through the indices and add
    # The difference between the numbers together
    for i in range(n):
        sum += abs(int(rightlis[i]) - int(leftlis[i]))
    return str(sum)


def sortdat(file: str) -> str:
    '''
    Checks how often an element from the left
    column of a given file is in the right column.
    Afterwards multiplies the number with the times it appears
    and finally adds those together.
    '''

    # We once again begin by reading out the file
    leftlis, rightlis = [], []
    with open(file) as page:
        for line in page:
            left, right = line.split(" ", 1)
            left = left.strip()
            right = right.strip(" \n")
            leftlis.append(left)
            rightlis.append(right)
    sum = 0

    # And then count how often each number
    # from the left list is in the right one.
    # We multiply the number with it and then
    # add it up
    for i in leftlis:
        sum += int(i) * rightlis.count(i)
    return str(sum)


if __name__ == "__main__":
    print(sortdat("locations.txt"))
