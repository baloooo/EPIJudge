from test_framework import generic_test

'''
def reverse_ll(self, head):
    pass

def reverse_k_sublists(head, k):
    pass
'''
class ListNode(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next

def reverse_sublist(head, start, finish):
    # TODO - you fill in here.
    if start == finish or head is None or head.next is None:
        return head
    orig_head = first_half = ListNode(None, head)
    cur_head = head
    for _ in range(1, start):
        first_half = cur_head
        cur_head = cur_head.next

    # reverse
    prev, cur = cur_head, cur_head.next
    for _ in range(finish - start):
        next = cur.next
        cur.next = prev
        prev, cur = cur, next

    # stich
    new_head = first_half.next
    first_half.next = prev
    new_head.next = cur

    return orig_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))
