from test_framework import generic_test

class ListNode():
    def __init__(self, data, next):
        self.data = data
        self.next = next

def merge_two_sorted_lists(l1, l2):
    # TODO - you fill in here.
    orig_head = cur_head = ListNode(None, None)
    while l1 and l2:
        if l1.data <= l2.data:
            cur_head.next = l1
            l1 = l1.next
        else:
            cur_head.next = l2
            l2 = l2.next
        cur_head = cur_head.next

    if l1:
        cur_head.next = l1
    if l2:
        cur_head.next = l2
    return orig_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
