from treenode import TreeNode

# 求二叉树所有节点的个数


def count_node(tn):
    if tn is None:
        return 0

    return count_node(tn.left) + count_node(tn.right) + 1


tn = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, TreeNode(6), TreeNode(7)))
print(count_node(tn))
