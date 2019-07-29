from treenode import TreeNode


def is_mirror(tn1, tn2):
    if tn1 is None and tn2 is None:
        return True

    elif tn1 is None and tn2 is not None:
        return False

    elif tn1 is not None and tn2 is None:
        return False

    else:
        if not tn1.val == tn2.val:
            return False
        else:
            return is_mirror(tn1.left, tn2.right) and is_mirror(tn1.right, tn2.left)


treenode = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))

# 判断treenode是否是镜像对称，可以将两个treenode都穿入is_mirror这个函数中
print(is_mirror(treenode, treenode))