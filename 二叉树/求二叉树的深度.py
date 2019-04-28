
import queue
from treenode import TreeNode

# 递归版本
def tree_depth(pRoot):
    if pRoot==None:
        return 0

    depth_left = tree_depth(pRoot.left)
    depth_right = tree_depth(pRoot.right)

    return max(depth_left, depth_right) + 1


# 非递归版本
def tree_depth2(pRoot):
    if pRoot == None:
        return 0

    q = queue.Queue()
    q.put(pRoot)

    cur = 1
    node = 0
    level = 0

    while not q.empty():
        while cur:
            tmpNode = q.get()
            cur -= 1

            if tmpNode.left:
                node += 1
                q.put(tmpNode.left)
            if tmpNode.right:
                node += 1
                q.put(tmpNode.right)

        level += 1
        cur = node
        node = 0

    return level


if __name__ == '__main__':
    root = TreeNode(3)
    left = TreeNode(4)
    right = TreeNode(5)
    root.left = left
    root.right = right

    print(tree_depth(root))
    print(tree_depth2(root))