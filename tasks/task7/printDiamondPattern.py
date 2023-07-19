def printDiamondPattern(rows: int) -> None:
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        diamonds = "* " * i
        print(spaces + diamonds)

    for i in range(rows - 1, 0, -1):
        spaces = " " * (rows - i)
        diamonds = "* " * i
        print(spaces + diamonds)

