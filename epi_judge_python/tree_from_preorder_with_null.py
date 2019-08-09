import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def reconstruct_preorder(preorder):
    def _deserialize(preorder_iter):
        cur = next(preorder_iter)
        if cur is None:
            return

        root = TreeNode(cur)
        root.left = _deserialize(preorder_iter)
        root.right = _deserialize(preorder_iter)

        return root

    preorder_iter = iter(preorder)
    return _deserialize(preorder_iter)


@enable_executor_hook
def reconstruct_preorder_wrapper(executor, data):
    data = [None if x == 'null' else int(x) for x in data]
    return executor.run(functools.partial(reconstruct_preorder, data))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_with_null.py",
                                       'tree_from_preorder_with_null.tsv',
                                       reconstruct_preorder_wrapper))


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

['1', '2', '#', '#', '3', '4', '#', '#', '5', '#', '#']
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        tree_repr = []
        self._serialize(root, tree_repr)
        return ' '.join(tree_repr)

    def _serialize(self, root, tree_repr):
            if root is None:
                tree_repr.append('#')
                return
            tree_repr.append(str(root.val))
            self._serialize(root.left, tree_repr)
            self._serialize(root.right, tree_repr)


    def _deserialize(self, data):
        if data[self.data_idx] == '#':
            self.data_idx += 1
            return None
        root = TreeNode(data[self.data_idx])
        self.data_idx += 1
        root.left = self._deserialize(data)
        root.right = self._deserialize(data)
        return root


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def _deserialize(self, data):
            if data[self.data_idx] == '#':
                self.data_idx += 1
                return None
            root = TreeNode(data[self.data_idx])
            self.data_idx += 1
            root.left = self._deserialize(data)
            root.right = self._deserialize(data)
            return root

        data_iter = None
        return _deserialize(data_iter)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))