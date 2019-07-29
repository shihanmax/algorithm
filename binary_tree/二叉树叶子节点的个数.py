from treenode import TreeNode
# 注意求的是叶子结点的个数！！


def count_leaf_node(tn):
    if tn is None:
        return 0
    if tn.leaf is None and tn.right is None:
        return 1  # 此时的节点是一个叶子结点

    return count_leaf_node(tn.leaf) + count_leaf_node(tn.right)


tn = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, TreeNode(6), TreeNode(7)))
print(count_leaf_node(tn))
