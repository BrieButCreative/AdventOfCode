def sortdis(file: str) -> str:
    '''
    Ermittelt aus dem Inhalt der gegebenen Datei
    wie weit die jeweils kleinsten Werte auseinander liegen.

    >>> sortdis("test_locations.txt")
    "11"
    '''

    leftlis, rightlis = [], []
    with open(file) as page:
        for line in page:
            left, right = line.split(" ", 1)
            left = left.strip()
            right = right.strip(" \n")
            leftlis.append(left)
            rightlis.append(right)
    rightlis, leftlis = sorted(rightlis), sorted(leftlis)
    n = len(rightlis)
    sum = 0
    for i in range(n):
        sum += abs(int(rightlis[i]) - int(leftlis[i]))
    return str(sum)


def sortdat(file: str) -> str:
    leftlis, rightlis = [], []
    with open(file) as page:
        for line in page:
            left, right = line.split(" ", 1)
            left = left.strip()
            right = right.strip(" \n")
            leftlis.append(left)
            rightlis.append(right)
    sum = 0
    for i in leftlis:
        sum += int(i) * rightlis.count(i)
    return str(sum)


if __name__ == "__main__":
    print(sortdat("locations.txt"))
