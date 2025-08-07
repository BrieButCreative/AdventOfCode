def table_reader(file: str) -> list[str]:
    '''
    Transforms the stuff from inside a file into a two-dimensional array.    
    '''
    return open(file).read().splitlines()


if __name__ == "__main__":
    print(table_reader("testPuzzle.txt")[3][6])
