from test_framework import generic_test


class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def get_bt(self, preorder, inorder, inorder_min, inorder_max):
        if inorder_min > inorder_max:
            return
        root = TreeNode(preorder[self.pre_idx])
        self.pre_idx += 1
        root_idx = inorder.index(root.data)

        root.left = self.get_bt(preorder, inorder, inorder_min, root_idx - 1)

        root.right = self.get_bt(preorder, inorder, root_idx + 1, inorder_max)

        return root

def binary_tree_from_preorder_inorder(preorder, inorder):
    sol = Solution()
    sol.pre_idx = 0
    return sol.get_bt(preorder, inorder, 0, len(inorder)-1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_inorder.py",
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
