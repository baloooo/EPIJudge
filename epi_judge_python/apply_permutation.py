from test_framework import generic_test


def apply_permutation(perm, arr):
    # TODO - you fill in here.
    for perm_idx, arr_idx in enumerate(perm):
        prev_dislocated = arr[perm_idx]
        while arr_idx >= 0:
            cur_dislocated = arr[arr_idx]
            arr[arr_idx] = prev_dislocated
            perm[perm_idx] = (-1) * arr_idx
            arr_idx = perm[arr_idx]
            prev_dislocated = cur_dislocated

    return


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("apply_permutation.py",
                                       "apply_permutation.tsv",
                                       apply_permutation_wrapper))
