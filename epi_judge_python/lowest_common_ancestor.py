import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

def _lca(tree, node0, node1):
    if tree is None:
        return
    tree_left, tree_right = None, None
    if tree.left:
        tree_left = _lca(tree.left, node0, node1)
    if tree.right:
        tree_right = _lca(tree.right, node0, node1)

    if (tree in [node0, node1] and (tree_left or tree_right)):
        return tree

    if (tree_left == node0 and tree_right == node1) or (tree_left == node1 and tree_right == node0):
        return tree

    if tree in [node0, node1]:
        #print('found node', tree.data)
        return tree

    return tree_left or tree_right

def lca(tree, node0, node1):
    '''
    are there any duplicates of node0/1: no
    does lca always exist(node0 and node1 will exist in the tree): yes
    '''
    return _lca(tree, node0, node1)


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
