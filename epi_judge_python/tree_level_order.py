from test_framework import generic_test


def binary_tree_depth_order(tree):
    # TODO - you fill in here.
    # BFT
    if not tree:
        return []
    lvl_order_list = []
    cur_level =[tree]
    while len(cur_level) != 0:
        # lvl_order_list.append(cur_level[:])
        lvl_order_list.append([])
        next_level = []
        for node in cur_level:
            lvl_order_list[-1].append(node.data)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        cur_level = next_level
    return lvl_order_list


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))
