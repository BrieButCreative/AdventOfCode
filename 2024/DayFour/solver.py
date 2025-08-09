from cheater import table_reader


def x_mess(file: str) -> int:
    '''
    Finds all apparences of the word 'mas'
    alligned as an X in the file.

    >>> x_mess("testPuzzle.txt")
    9
    '''

    word_search, apparences = table_reader(file), 0
    rows, columns = len(word_search), len(word_search[0])
    for row in range(1, (rows - 1)):
        for column in range(1, (columns - 1)):
            if word_search[row][column] == "a":
                left_cross, right_cross = False, False
                if word_search[row - 1][column - 1] == "m" \
                        and word_search[row + 1][column + 1] == "s" \
                        or word_search[row - 1][column - 1] == "s" \
                        and word_search[row + 1][column + 1] == "m":
                    left_cross = True
                if word_search[row + 1][column - 1] == "m" \
                        and word_search[row - 1][column + 1] == "s" \
                        or word_search[row + 1][column - 1] == "s" \
                        and word_search[row - 1][column + 1] == "m":
                    right_cross = True
                if left_cross and right_cross:
                    apparences += 1
    return apparences


if __name__ == "__main__":
    print(x_mess("Puzzle.txt"))
