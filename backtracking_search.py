import copy

from csp import getRemainingValues
from minimum_remaining_value import *
from forward_checking import *


def backtracking_search(sudoku, expanded_nodes, rv, position_ver, version):
    # unassigned position
    position = [0, 0]

    if position_ver == 0:
        if not find_unassigned(sudoku, position):
            print(expanded_nodes)
            print("SOLUTION")
            for row in sudoku:
                print(row)
            return True

    if position_ver == 1:
        if (not minimum_remaining_value(rv, position)):
            print(expanded_nodes)
            print("SOLUTION")
            for row in sudoku:
                print(row)
            return True

    u_row = position[0]
    u_col = position[1]
    expanded_nodes[0] += 1


    if version == 0:
        for variable in rv[u_row][u_col]:
            sudoku[u_row][u_col] = variable
            rv = getRemainingValues(sudoku)

            if backtracking_search(sudoku, expanded_nodes, rv, position_ver, 0):
                return True
            sudoku[u_row][u_col] = 0

    if version == 1:
        for variable in rv[u_row][u_col]:
            sudoku[u_row][u_col] = variable
            cpy = copy.deepcopy(rv)
            rv = getRemainingValues(sudoku)

            if forward_checking(rv):
                if backtracking_search(sudoku, expanded_nodes, rv, position_ver, 1):
                    return True
            sudoku[u_row][u_col] = 0
            rv = cpy

    return False


def find_unassigned(sudoku, position):
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                position[0] = row
                position[1] = col
                return True
    return False

