from test_framework import generic_test

'''
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    
'''

def matrix_in_spiral_order(square_matrix):
    # TODO - you fill in here.
    if not square_matrix:
        return []
    spiral_matrix = []
    left_wall, right_wall, top_wall, bottom_wall = 0, len(square_matrix[0])-1, 0, len(square_matrix)-1
    while left_wall <= right_wall and top_wall <= bottom_wall:
        # left to right
        for col_idx in range(left_wall, right_wall+1):
            spiral_matrix.append(square_matrix[top_wall][col_idx])

        top_wall += 1
        # top to bottom
        for row_idx in range(top_wall, bottom_wall+1):
            spiral_matrix.append(square_matrix[row_idx][right_wall])

        right_wall -= 1
        # right to left
        for col_idx in range(right_wall, left_wall - 1, -1):
            spiral_matrix.append(square_matrix[bottom_wall][col_idx])

        bottom_wall -= 1
        # bottom to top
        for row_idx in range(bottom_wall, top_wall - 1, -1):
            spiral_matrix.append(square_matrix[row_idx][left_wall])

        left_wall += 1
    return spiral_matrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))
