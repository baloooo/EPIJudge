from test_framework import generic_test


def inorder_traversal(tree):
    if tree is None:
        return []
    call_stack = []
    inorder_traversal = []
    call_stack.append(tree)
    while call_stack:
        root = call_stack.pop()
        if isinstance(root, int) or isinstance(root, str):
            inorder_traversal.append(root)
        elif root.left is None and root.right is None:
            inorder_traversal.append(root.data)
        else:
            if root.right:
                call_stack.append(root.right)
            call_stack.append(root.data)
            if root.left:
                call_stack.append(root.left)
    return inorder_traversal


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_inorder.py", 'tree_inorder.tsv',
                                       inorder_traversal))
