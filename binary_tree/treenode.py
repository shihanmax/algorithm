

# 二叉树TreeNode类

class TreeNode(object):

    def __init__(self, val, left=None, right=None):
        self.val = val
        if not left:
            self.left = None
        else:
            self.left = left

        if not right:
            self.right = None
        else:
            self.right = right

