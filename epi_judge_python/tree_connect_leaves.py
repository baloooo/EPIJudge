import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

def _get_leaves(root, leaves):
    if root is None:
        return
    if root.left is None and root.right is None:
        # print('type of root is', type(root))
        # print('root is ', root)
        leaves.append(root)
        return
    _get_leaves(root.left, leaves)
    _get_leaves(root.right, leaves)

    return


def create_list_of_leaves(root):
    leaves = []
    _get_leaves(root, leaves)
    return leaves


@enable_executor_hook
def create_list_of_leaves_wrapper(executor, tree):
    result = executor.run(functools.partial(create_list_of_leaves, tree))

    if any(x is None for x in result):
        raise TestFailure("Result list can't contain None")
    return [x.data for x in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_connect_leaves.py",
                                       "tree_connect_leaves.tsv",
                                       create_list_of_leaves_wrapper))
