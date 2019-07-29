from treenode import TreeNode
# !!!还有疑问，逻辑无误，但结果好像不对


def _is_sub(tn_1, tn_2):
    """

    :param tn_1: root treeNode
    :param tn_2: sub treeNode
    :return: bool
    """

    if tn_1 is None:
        return False

    if tn_2 is None:
        return True

    if tn_1.val != tn_2.val:
        return False

    return _is_sub(tn_1.left, tn_2.left) and _is_sub(tn_1.right, tn_2.right)


def is_sub_structure(tn_1, tn_2):
    result = False
    
    if tn_1 is not None and tn_2 is not None:
        if tn_1.val == tn_2.val:  # 只有在两个节点的值相同时，才调用子函数 _is_sub()
            result = _is_sub(tn_1, tn_2)

        if not result:
            is_sub_structure(tn_1.left, tn_2)

        if not result:
            is_sub_structure(tn_1.right, tn_2)

    return result


tn = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, TreeNode(6), TreeNode(7)))
tn_s = TreeNode(2, None, TreeNode(4))

print(is_sub_structure(tn, tn_s))