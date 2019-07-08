from treenode import TreeNode


def rebuild_tree(pre_order, in_order, length):
    """
    根据前序遍历和中序遍历重建二叉树
    所构建的二叉树是否唯一？参考：https://www.cnblogs.com/jiaxin359/p/9512348.html
    :param pre_order:
    :param in_order:
    :param length:
    :return:
    """
    if len(pre_order) == 0 or len(in_order) == 0 or length <= 0:
        return None

    i = 0
    tn = pre_order[0]
    root = TreeNode(tn)

    while i < length and in_order[i] != tn:
        i += 1

    if i == length:
        return None

    root.left = rebuild_tree(pre_order[1:], in_order, i)
    root.right = rebuild_tree(pre_order[i+1:], in_order[i+1:], length-i-1)
    return root


pre_order = [1, 2, 3, 4, 5, 6, 7]
in_order = [3, 2, 4, 1, 6, 5, 7]

rebuild_tree(pre_order, in_order, 7)
