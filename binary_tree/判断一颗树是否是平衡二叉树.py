from treenode import TreeNode

# 平衡的定义：左子树和右子树的最大高度差不大于1


def tree_depth(tn):
    if tn is None:
        return 0

    depth_left = tree_depth(tn.left)
    depth_right = tree_depth(tn.right)

    return max(depth_left, depth_right) + 1


def is_balanced_binary_tree(tn):
    if tn is None:
        return True

    left = tree_depth(tn.left)
    right = tree_depth(tn.right)

    diff = left - right

    if diff > 1 or diff < -1:
        return False

    return is_balanced_binary_tree(tn.left) and is_balanced_binary_tree(tn.right)


treenode = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
print(is_balanced_binary_tree(treenode))