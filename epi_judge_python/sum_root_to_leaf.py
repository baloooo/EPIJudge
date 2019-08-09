from test_framework import generic_test

# class Sol(object):
#     def get_sum(self, root, cur_sum):
#         if root is None:
#             return
#         if root.left is None and root.right is None:
#             self.sums.append(''.join(cur_sum) + str(root.data))
#             return
#         cur_sum.append(str(root.data))
#         self.get_sum(root.left, cur_sum)
#         self.get_sum(root.right, cur_sum)
#         cur_sum.pop()
#
# def sum_root_to_leaf(tree, partial_path_sum=0):
#     # TODO - you fill in here.
#     sol = Sol()
#     sol.sums = []
#     cur_sum = []
#     sol.get_sum(tree, cur_sum)
#     total_sum = 0
#     for cur_sum in sol.sums:
#         total_sum += int(cur_sum, 2)
#    return total_sum

def sum_root_to_leaf(tree, partial_path_sum=0):
    if tree is None: return 0
    partial_path_sum = (2 * partial_path_sum) + tree.data
    if tree.left is None and tree.right is None:
        return partial_path_sum
    return sum_root_to_leaf(tree.left, partial_path_sum) + sum_root_to_leaf(tree.right, partial_path_sum)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "sum_root_to_leaf.py", 'sum_root_to_leaf.tsv', sum_root_to_leaf))
