from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment):
    # TODO - you fill in here.
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


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_sudoku.py",
                                       "is_valid_sudoku.tsv", is_valid_sudoku))
