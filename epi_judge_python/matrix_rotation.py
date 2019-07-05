from test_framework import generic_test

'''
[
    [1, 2,  3, 4],
    [5, 6,  7, 8],
    [9, 10, 11, 12],
    [13,14, 15, 16]
]
[
    [13, 9,  5, 1],
    [14, 10, 6, 2],
    [15, 11, 7, 3],
    [16, 12, 8, 4]
]
The first insight is that we c.rn perform the
rotation in a layer-by-layer fashion-different layers canbe processed independently. Furthermore,
within a layer, we can exchange groups of four elements at a time to perform the rotation, e.g.,
send L to 4's location, 4 to 16's location,16 to 13's location, and L3 to 1's location, then send 2 to 8's
location, 8 to 15's location, 15 to 9's location, and 9 to 2's location, etc. The program below works
its way into the center of the array from the outermost layers, performing exchanges within a layer
iteratively using the four-way swap just described.
'''

def rotate_matrix(square_matrix):
    # TODO - you fill in here.
    # swap top and bottom rows
    for col_id in range(square_matrix[0]):
        square_matrix[0][col_id], square_matrix[-1][col_id] = square_matrix[-1][col_id], square_matrix[0][col_id]

    # swap acrosss left diagnol
    for row_id in range(len(square_matrix)):
        for col_id in range(len(square_matrix[0])):
            pass
    return


def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_rotation.py",
                                       'matrix_rotation.tsv',
                                       rotate_matrix_wrapper))
