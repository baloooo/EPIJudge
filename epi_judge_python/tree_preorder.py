from test_framework import generic_test


def preorder_traversal(tree):
    preorder_traversal = []
    call_stack = []
    while call_stack:
        pass
    return preorder_traversal


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_preorder.py", 'tree_preorder.tsv',
                                       preorder_traversal))
