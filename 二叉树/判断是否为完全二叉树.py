from queue import Queue
from treenode import TreeNode


def is_complete_tree(tn):
    # 判断tn是否是完全二叉树，注意完全二叉树的定义
    if tn is None:
        return True

    flag = False  # flag为True是，表示后面不能再有节点了

    q = Queue()
    q.put(tn)

    while not q.empty():
        tmp = q.get()

        # 左子节点或右子节点为空时，就将flag设置为True

        if tmp.left and not flag:
            q.put(tmp.left)
        elif tmp.left and flag:
            return False
        elif not tmp.left:
            flag = True

        if tmp.right and not flag:
            q.put(tmp.right)
        elif tmp.right and flag:
            return False
        elif not tmp.right:
            flag = True

    return True


tn = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, TreeNode(6), None))
print(is_complete_tree(tn))