from treenode import TreeNode
# 判断一课二叉树是否平衡
# 平衡指的是这棵树任意两个叶子结点到根结点的距离之差不大于1


def get_max_depth(tn):
    if tn is None:
        return 0
    return 1 + max(get_max_depth(tn.left), get_max_depth(tn.right))


def get_min_depth(tn):
    if tn is None:
        return 0
    return 1 + min(get_min_depth(tn.left), get_min_depth(tn.right))


def is_tree_balance(tn):
    """
    此题可以求二叉树的最大高度和最小高度，二者之差小于等于1即可满足平衡条件
    :param tn:
    :return: bool
    """
    return (get_max_depth(tn) - get_min_depth(tn)) <= 1


treenode = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), )

print(is_tree_balance(treenode))