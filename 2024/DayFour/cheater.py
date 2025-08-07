def table_reader(file: str) -> list[str]:
    '''
    Transforms the stuff from inside a file into a two-dimensional array.    
    '''
    word_table = []
    for i in open(file).read().splitlines():
        word_table.append(i.lower())
    return word_table


def word_finder(file: str, word: str) -> int:
    '''
    Counts the apparences of the given word
    in the given file.

    >>> word_finder("testPuzzle.txt", "XMAS")
    18
    '''

    instances = 0
    word = word.lower()
    word_length = len(word)
    if word_length == 0:
        return
    input = table_reader(file)
    rows, columns = len(input), len(input[0])
    for row in range(rows):
        for column in range(columns):
            if input[row][column] == word[0]:
                instances += layout(input, row, column, rows, columns,
                                    word[1:], word_length - 1)
    return instances


def layout(table: list[str], row: int, column: int, max_rows: int,
           max_columns: int, word: str, length: int) -> int:
    '''
    Function to outsource the blattera of if statements.
    Basically tests if the given word exist in any direction.
    '''
    occurences = 0
    if row - length >= 0:
        for i in range(length):
            if table[row - 1 - i][column] == word[i]:
                continue
            break
        else:
            occurences += 1
    if row + length < max_rows:
        for i in range(length):
            if table[row + 1 + i][column] == word[i]:
                continue
            break
        else:
            occurences += 1
    if column - length >= 0:
        for i in range(length):
            if table[row][column - 1 - i] == word[i]:
                continue
            break
        else:
            occurences += 1
    if column + length < max_columns:
        for i in range(length):
            if table[row][column + 1 + i] == word[i]:
                continue
            break
        else:
            occurences += 1
    if row - length >= 0 and column - length >= 0:
        for i in range(length):
            if table[row - 1 - i][column - 1 - i] == word[i]:
                continue
            break
        else:
            occurences += 1
    if row - length >= 0 and column + length < max_columns:
        for i in range(length):
            if table[row - 1 - i][column + 1 + i] == word[i]:
                continue
            break
        else:
            occurences += 1
    if row + length < max_rows and column - length >= 0:
        for i in range(length):
            if table[row + 1 + i][column - 1 - i] == word[i]:
                continue
            break
        else:
            occurences += 1
    if row + length < max_rows and column + length < max_columns:
        for i in range(length):
            if table[row + 1 + i][column + 1 + i] == word[i]:
                continue
            break
        else:
            occurences += 1
    return occurences


if __name__ == "__main__":
    print(word_finder("Puzzle.txt", "xmas"))
