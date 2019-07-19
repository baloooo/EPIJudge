from test_framework import generic_test

class ListNode(object):
    def __init__(self, data, next):
        self.val = data
        self.next = next

def remove_duplicates(head):
    # 1 -> 1 -> 2 -> 3 -> 3
    # 1 -> 1
    # TODO - you fill in here.
    if head is None or head.next is None:
        return head
    orig_head = head
    # 1 -> 1 -> 2 -> 3 -> 3
    # 1 -> 2 -> 3 -> 3
    while head.next is not None:
        if head.next.data == head.data:
            head.next = head.next.next
        else:
            head = head.next
    return orig_head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "remove_duplicates_from_sorted_list.py",
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
