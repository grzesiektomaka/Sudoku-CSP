from const import *


def minimum_remaining_value(rv, position):
    min_val = 10

    for row in range(DIM):
        for col in range(DIM):
            if rv[row][col] != -1:
                val_len = len(rv[row][col])
                if val_len < min_val:
                    min_val = val_len
                    position[0] = row
                    position[1] = col

    if min_val == 10:
        return False
    else:
        return True
