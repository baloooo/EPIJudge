from test_framework import generic_test


def cyclically_right_shift_list(head, k):
    # TODO - you fill in here.
    # 2 -> 3 -> 5 -> 3 -> 2
    # k = 3
    # 5 -> 3 -> 2 -> 2 -> 3
    # k = 2
    # 3 -> 2 -> 2 -> 3 -> 5
    if k == 0 or head is None or head.next is None:
        return head
    return None


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("list_cyclic_right_shift.py",
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
