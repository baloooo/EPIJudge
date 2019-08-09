import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def get_len(node):
    node_len = 0
    while node.parent is not None:
        node = node.parent
        node_len += 1

    return node_len

def lca(closer_node, farther_node):
    closer_node_len = get_len(closer_node)
    farther_node_len = get_len(farther_node)
    # bring the longer node up k times where k is the diff b/w node0_len and node1_len
    if farther_node_len < closer_node_len:
        closer_node, farther_node = farther_node, closer_node
        closer_node_len, farther_node_len = farther_node_len, closer_node_len
    while farther_node_len != closer_node_len:
        farther_node = farther_node.parent
        farther_node_len -= 1
    # traverse towards root one hop at a time and return the first node where both meet
    while farther_node != closer_node:
        closer_node = closer_node.parent
        farther_node = farther_node.parent

    return closer_node


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor_with_parent.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
