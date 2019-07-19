import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


class ListNode(object):
    def __init__(self, data, next):
        self.data = data
        self.next = next


def list_pivoting(head, k):
    # TODO - you fill in here.
    '''
    10, 50, 20, 100, 150, 5, 7, 11, 190
    k = 50
    10, 50, 20, 5, 7, 11, 100, 150, 190
    '''
    if head is None or head.next is None:
        return head
    less_than_k = orig_less_than_k = ListNode(None, None)
    greaeter_than_k = orig_greater_than_k = ListNode(None, None)
    print('K: ', k)
    while head:
        print(head.data)
        if head.data < k:
            less_than_k.next = head
            less_than_k = less_than_k.next
            head = head.next
            less_than_k.next = None
        else:
            greaeter_than_k.next = head
            greaeter_than_k = greaeter_than_k.next
            head = head.next
            greaeter_than_k.next = None
    less_than_k.next = orig_greater_than_k.next

    head = orig_less_than_k.next
    print('printing list')
    while head is None:
        print(head.data)
    return orig_less_than_k.next


def linked_to_list(l):
    v = list()
    while l is not None:
        v.append(l.data)
        l = l.next
    return v


@enable_executor_hook
def list_pivoting_wrapper(executor, l, x):
    original = linked_to_list(l)

    l = executor.run(functools.partial(list_pivoting, l, x))

    pivoted = linked_to_list(l)
    mode = -1
    for i in pivoted:
        if mode == -1:
            if i == x:
                mode = 0
            elif i > x:
                mode = 1
        elif mode == 0:
            if i < x:
                raise TestFailure('List is not pivoted')
            elif i > x:
                mode = 1
        else:
            if i <= x:
                raise TestFailure('List is not pivoted')

    if sorted(original) != sorted(pivoted):
        raise TestFailure('Result list contains different values')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("pivot_list.py", 'pivot_list.tsv',
                                       list_pivoting_wrapper))
