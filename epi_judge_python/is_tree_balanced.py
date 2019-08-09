from test_framework import generic_test


def get_height(tree):
    if tree is None:
        return 0
    left_subtree_height = get_height(tree.left)
    if left_subtree_height is False:
        return False
    right_subtree_height = get_height(tree.right)
    if right_subtree_height is False:
        return False
    if abs(right_subtree_height - left_subtree_height) > 1:
        return False

    return 1 + max(left_subtree_height, right_subtree_height)

def is_balanced_binary_tree(tree):
    if tree is None:
        return True
    return bool(get_height(tree))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
