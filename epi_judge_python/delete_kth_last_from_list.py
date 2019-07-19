from test_framework import generic_test

class ListNode(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next

# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(head, k):
    # TODO - you fill in here.
    if head is None:
        return
    # start cur_ptr from cur_head
    orig_head = fw_ptr = cur_ptr = ListNode(None, head)
    # move fw_ptr k steps ahead
    for _ in range(k):
        fw_ptr = fw_ptr.next
    # move both cur_ptr and fw_ptr one step at a time, until fw_ptr.next is not None
    while fw_ptr.next is not None:
        fw_ptr = fw_ptr.next
        cur_ptr = cur_ptr.next
    # node to delete is the node ahead of cur_ptr, delete it
    cur_ptr.next = cur_ptr.next.next
    return orig_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("delete_kth_last_from_list.py",
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
