import copy
import functools
import math

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def solve_sudoku(partial_assignment):
    # TODO - you fill in here.
    '''
    [
        [1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9],

    ]
    '''
    # check rows
    for row_idx in range(len(partial_assignment)):
        row_set = set()
        for col_idx in range(len(partial_assignment[0])):
            if partial_assignment[row_idx][col_idx] in row_set:
                return False
            else:
                if partial_assignment[row_idx][col_idx] != 0:
                    row_set.add(partial_assignment[row_idx][col_idx])
    print('rows ok')
    # check cols
    for col_idx in range(len(partial_assignment[0])):
        col_set = set()
        for row_idx in range(len(partial_assignment)):
            if partial_assignment[row_idx][col_idx] in col_set:
                return False
            else:
                if partial_assignment[row_idx][col_idx] != 0:
                    col_set.add(partial_assignment[row_idx][col_idx])
    print('cols ok')
    # check cols
    # check 3*3 boxes
    for row_idx in range(0, len(partial_assignment), 3):
        for col_idx in range(0, len(partial_assignment[0]), 3):
            cur_box = set()
            for cur_row_idx in range(row_idx, row_idx+3):
                for cur_col_idx in range(col_idx, col_idx+3):
                    if partial_assignment[cur_row_idx][cur_col_idx] in cur_box:
                        return False
                    else:
                        if partial_assignment[cur_row_idx][cur_col_idx] != 0:
                            cur_box.add(partial_assignment[cur_row_idx][cur_col_idx])
    print('boxes ok')
    return True


def assert_unique_seq(seq):
    seen = set()
    for x in seq:
        if x == 0:
            raise TestFailure('Cell left uninitialized')
        if x < 0 or x > len(seq):
            raise TestFailure('Cell value out of range')
        if x in seen:
            raise TestFailure('Duplicate value in section')
        seen.add(x)


def gather_square_block(data, block_size, n):
    block_x = (n % block_size) * block_size
    block_y = (n // block_size) * block_size

    return [
        data[block_x + i][block_y + j] for j in range(block_size)
        for i in range(block_size)
    ]


@enable_executor_hook
def solve_sudoku_wrapper(executor, partial_assignment):
    solved = copy.deepcopy(partial_assignment)

    executor.run(functools.partial(solve_sudoku, solved))

    if len(partial_assignment) != len(solved):
        raise TestFailure('Initial cell assignment has been changed')

    for (br, sr) in zip(partial_assignment, solved):
        if len(br) != len(sr):
            raise TestFailure('Initial cell assignment has been changed')
        for (bcell, scell) in zip(br, sr):
            if bcell != 0 and bcell != scell:
                raise TestFailure('Initial cell assignment has been changed')

    block_size = int(math.sqrt(len(solved)))

    for i in range(len(solved)):
        assert_unique_seq(solved[i])
        assert_unique_seq([row[i] for row in solved])
        assert_unique_seq(gather_square_block(solved, block_size, i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sudoku_solve.py", 'sudoku_solve.tsv',
                                       solve_sudoku_wrapper))
