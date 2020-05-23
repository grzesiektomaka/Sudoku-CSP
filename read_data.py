import csv

def read_data(csv_file_name, id):
    sudoku_board = [[0 for row in range(0,9)] for col in range(0,9)]
    with open(csv_file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        next(csv_reader)
        for count, line in enumerate(csv_reader, start=1):
            if count == id:
                print(line[0] + '  |  ' + line[1] + '  |  ' + line[2])
                for row in range(9):
                    for col in range(9):
                        k = col + 9 * row
                        if (line[2][k] == '.') :
                             sudoku_board[row][col] = 0
                        else:
                            sudoku_board[row][col] = int(line[2][k])
    return sudoku_board