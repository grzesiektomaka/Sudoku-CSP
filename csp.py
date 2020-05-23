from const import *

def selectDomain(row, col, sudoku):
    domain = [1,2,3,4,5,6,7,8,9]
    for i in range(DIM):
        if sudoku[row][i] != 0:
            if sudoku[row][i] in domain:
                domain.remove(sudoku[row][i])

    for i in range(DIM):
        if sudoku[i][col] != 0:
            if sudoku[i][col] in domain:
                domain.remove(sudoku[i][col])

    boxRow = row - row % 3
    boxCol = col - col % 3

    for i in range(3):
        for j in range(3):
            if sudoku[boxRow + i][boxCol + j] != 0:
                if sudoku[boxRow + i][boxCol + j] in domain:
                    domain.remove(sudoku[boxRow + i][boxCol + j])
    return domain

def getRemainingValues(sudoku):
    rv = [[0 for row in range(0, DIM)] for col in range(0, DIM)]
    for row in range(DIM):
        for col in range(DIM):
            if sudoku[row][col] != 0:
                rv[row][col] = -1
            else:
                rv[row][col] = selectDomain(row, col, sudoku)
    return rv
