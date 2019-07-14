import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0, l1):
    # TODO - you fill in here.
    if l0 is None or l1 is None:
        return
    tail_l0 = tail_l1 = None

    len_l0 = len_l1 = 0
    head = l0
    while head is not None:
        len_l0 += 1
        tail_l0 = head
        head = head.next
    head = l1
    while head is not None:
        tail_l1 = head
        len_l1 += 1
        head = head.next

    if tail_l0 != tail_l1:
        return None
    if len_l0 < len_l1:
        len_l0, len_l1 = len_l1, len_l0
        lo, l1 = l1, l0

    l0_head, l1_head = l0, l1
    for _ in range(len_l0 - len_l1):
        l0_head = l0_head.next

    while l0_head and l1_head:
        if l0_head == l1_head:
            return l0_head
        l0_head = l0_head.next
        l1_head = l1_head.next
    return None


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(
        functools.partial(overlapping_no_cycle_lists, l0, l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("do_terminated_lists_overlap.py",
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
