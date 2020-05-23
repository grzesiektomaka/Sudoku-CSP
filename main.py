import timeit


def main():

    SETUP_CODE = '''
from backtracking_search import backtracking_search
from read_data import read_data
from csp import getRemainingValues

id_list=22

sudoku = read_data('Sudoku.csv', id_list )
expanded_nodes=[0]
rv = getRemainingValues(sudoku)
    '''
    BACKTRACKING = '''
backtracking_search(sudoku, expanded_nodes, rv, 0, 0)
    '''

    BACKTRACKING_FC = '''
backtracking_search(sudoku, expanded_nodes, rv, 0, 1)
            '''

    BACKTRACKING_MRV = '''
backtracking_search(sudoku, expanded_nodes, rv, 1, 0)
    '''

    BACKTRACKING_MRV_FC = '''
backtracking_search(sudoku, expanded_nodes, rv, 1, 1)
        '''

    print('BACKTRACKING')
    backtracking = timeit.timeit(setup=SETUP_CODE, stmt=BACKTRACKING, number=1)
    print('Time: ')
    print(backtracking)

    print('BACKTRACKING_FC')
    backtracking_fc = timeit.timeit(setup=SETUP_CODE, stmt=BACKTRACKING_FC, number=1)
    print('Time: ')
    print(backtracking_fc)

    print('BACKTRACKING_MRV')
    backtracking_mrv = timeit.timeit(setup=SETUP_CODE, stmt=BACKTRACKING_MRV, number=1)
    print('Time: ')
    print(backtracking_mrv)

    print('BACKTRACKING_MRV_FC')
    backtracking_mrv_fc = timeit.timeit(setup=SETUP_CODE, stmt=BACKTRACKING_MRV_FC, number=1)
    print('Time: ')
    print(backtracking_mrv_fc)

main()
