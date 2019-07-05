from test_framework import generic_test


def generate_pascal_triangle(n):
    # TODO - you fill in here.
    pascal_trianlge = []
    if n == 0: return pascal_trianlge
    prev_row = [1]
    pascal_trianlge.append(prev_row)
    for _ in range(n-1):
        cur_row = [1] + [prev_row[cur_idx] + prev_row[cur_idx - 1] for cur_idx in range(1, len(prev_row))] + [1]
        pascal_trianlge.append(cur_row)
        prev_row = cur_row
    return pascal_trianlge


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("pascal_triangle.py",
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
