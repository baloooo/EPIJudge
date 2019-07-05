import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size, s):
    '''
    [a, c, b, b, c, a]
    [a, c, c, a, c, a]
    orig_idx = 4
    no_of_a = 2
    [d, d, c, c, d, d]
    [d, d, c, c, d, d]
    '''
    # TODO - you fill in here.
    # Delete bs traversing from L to R -> O(n)
    cur_idx, orig_idx = 0, 0
    number_of_a = 0
    for cur_idx in range(len(s)):
        if s[cur_idx] != 'b' and s[cur_idx] != "":
            s[orig_idx] = s[cur_idx]
            orig_idx += 1
            if s[cur_idx] == 'a':
                number_of_a += 1
    # Replace 'd' with two 'b's, traversing from R -> to Left in O(n)
    final_arr_len = orig_arr_idx = orig_idx + number_of_a - 1
    for cur_idx in range(orig_idx-1, -1, -1):
        if s[cur_idx] == 'a':
            s[orig_arr_idx], s[orig_arr_idx - 1] = 'd', 'd'
            orig_arr_idx -= 1
        else:
            s[orig_arr_idx] = s[cur_idx]

        orig_arr_idx -= 1

    return final_arr_len + 1


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("replace_and_remove.py",
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
