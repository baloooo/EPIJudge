from test_framework import generic_test


def is_linked_list_a_palindrome(head):
    # TODO - you fill in here.
    # 1 -> 2 -> 3 ->  4 ->  5 ->  6 -> 7 -> 8 -> 9
    # if fast.next is None odd no of nodes with slow on middle node, prev_to_slow.next = None and reverse second half upto(including) slow.next
    # else fast is None and slow is the next half so reverse up untill slow and prev_to_slow.next = None
    '''


    prev_to_slow = 4000
    slow = 5000
    fast = 9000

    1 -> 2 -> 3 ->  4
    5 ->
    6 <- 7 <- 8 <- 9

    prev = 9000
    cur = None
    next = None
    first_half = 1000
    second_half = 9000

    '''
    if head is None or head.next is None:
        return True
    # find mid
    slow = fast = head
    while fast and fast.next:
        prev_to_slow = slow
        slow = slow.next
        fast = fast.next.next
    prev_to_slow.next = None
    # reverse from mid to end
    prev, cur = None, slow if fast is None else slow.next
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    # compare node by node first half and second half
    first_half, second_half = head, prev
    while first_half and second_half:
        if first_half.data != second_half.data:
            return False
        first_half = first_half.next
        second_half = second_half.next
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_list_palindromic.py",
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
