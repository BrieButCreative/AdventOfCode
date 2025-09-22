def readout(file: str) -> list[tuple[int, list[int]]]:
    '''
    Transforms the contents from a file into a
    dictionary in the form {solution: [candidates]}
    '''
    result = []
    contents = open(file).read().splitlines()
    for line in contents:
        sub = line.split(":")
        second = [int(x) for x in sub[1].split()]
        result += [tuple((int(sub[0]), second))]
    return result


def BRUTEFORCE(file: str, concentration: bool = False) -> int:
    '''
    It makes me so angry that neither me, nor anyone
    we asked could find a non bruteforce solution >:(
    Im actually quite proud how I solved the concentration "problem";
    I just created a second boolean and opt ined the last operator.
    The code works free of this boolean, except when adding symbols.
    >>> BRUTEFORCE("testCalibrations.txt")
    3749
    >>> BRUTEFORCE("testCalibrations.txt", True)
    11387
    '''
    final = 0
    terms = readout(file)
    for term in terms:
        solution, operands = term
        empties = len(operands) - 1
        symbols = ["+"] * empties
        while True:
            testsol = operands[0]
            for i in range(empties):
                if (symbols[i] == "+"):
                    testsol += operands[i + 1]
                elif (symbols[i] == "||"):
                    testsol = int(str(testsol) + str(operands[i + 1]))
                else:
                    testsol *= operands[i + 1]
            if testsol == solution:
                final += solution
                break
            elif "+" not in symbols and "||" not in symbols:
                break
            for i in range(empties):
                if symbols[i] == "+":
                    symbols[i] = "||"
                    break
                elif symbols[i] == "||" and concentration:
                    symbols[i] = "*"
                    break
                symbols[i] = "+"
    return final


print(BRUTEFORCE("Calibrations.txt", True))
