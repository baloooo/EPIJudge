import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None, size=None):
        self.data = data
        self.left = left
        self.right = right
        self.size = size

def find_kth_node_binary_tree(root, k):
    if root is None:
        return
    while True:
        if root.left is None and root.right is None:
            return root

        root_left_subtree_size = root.left.size + 1 if root.left is not None else 1  # including root

        if root_left_subtree_size == k:
            return root
        elif root_left_subtree_size < k:
            # Go right
            root = root.right
            k = k - root_left_subtree_size
        else:
            # Go left
            root = root.left

# def find_kth_node_binary_tree(root, k):
#     if root is None:
#         return
#     if root.left is None and root.right is None:
#         return root
#
#     root_left_subtree_size = root.left.size + 1 if root.left is not None else 1  # including root
#
#     if root_left_subtree_size == k:
#         return root
#     elif root_left_subtree_size < k:
#         # Go right
#         return find_kth_node_binary_tree(root.right, k - root_left_subtree_size)
#     else:
        # Go left
#        return find_kth_node_binary_tree(root.left, k)


@enable_executor_hook
def find_kth_node_binary_tree_wrapper(executor, tree, k):
    def init_size(node):
        if not node:
            return 0
        node.size = 1 + init_size(node.left) + init_size(node.right)
        return node.size

    init_size(tree)

    result = executor.run(
        functools.partial(find_kth_node_binary_tree, tree, k))

    if not result:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("kth_node_in_tree.py",
                                       "kth_node_in_tree.tsv",
                                       find_kth_node_binary_tree_wrapper))
