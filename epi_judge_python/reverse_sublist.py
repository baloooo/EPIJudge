from test_framework import generic_test

'''
def reverse_ll(self, head):
    pass

def reverse_k_sublists(head, k):
    pass
'''

def reverse_sublist(L, start, finish):
    # TODO - you fill in here.
    for _ in range(1, start):
        pass
    return None


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))
