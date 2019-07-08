from treenode import TreeNode
from queue import Queue


def preorder_traversal(tn):
    # 前序遍历
    if tn is not None:
        print(tn.val)
        preorder_traversal(tn.left)
        preorder_traversal(tn.right)


def inorder_traversal(tn):
    # 中序遍历
    if tn is not None:
        inorder_traversal(tn.left)
        print(tn.val)
        inorder_traversal(tn.right)


def postorder_traversal(tn):
    # 后序遍历
    if tn is not None:
        postorder_traversal(tn.left)
        postorder_traversal(tn.right)
        print(tn.val)


def level_traversal(tn):
    # 层序遍历
    queue = Queue()

    queue.put(tn)
    while not queue.empty():
        tn = queue.get()
        if tn:
            print(tn.val)
            queue.put(tn.left)
            queue.put(tn.right)


tn = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, TreeNode(6), TreeNode(7)))
preorder_traversal(tn)
print('----')
inorder_traversal(tn)
print('----')
postorder_traversal(tn)
print('----')
level_traversal(tn)