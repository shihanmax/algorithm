from treenode import TreeNode


class Solution:
    def __init__(self):
        self.res = []

    def verticalTraversal(self, root):
        self.set_pos(root, 0, 0)
        self.print_node(root)

        res = sorted(self.res, key=lambda x: (x[1], -x[2], x[0]))
        
        final = []
        last_pos = [None, None]

        for i in res:
            val = i[0]
            pos = (i[1], i[2])
            if pos[0] == last_pos[0]:
                final[-1].append(val)

            else:
                final.append([val])
                last_pos = pos
        return final


    def set_pos(self, root, x, y):
        if not root:
            return

        root.val = (root.val, x, y)

        if root.left:
            self.set_pos(root.left, x - 1, y - 1)
        if root.right:
            self.set_pos(root.right, x + 1, y - 1)

    def print_node(self, root):

        # if not root:
        #     return

        self.res.append(root.val)

        if root.left:
            self.print_node(root.left)
        if root.right:
            self.print_node(root.right)


root = TreeNode(3)
root.left = TreeNode(9)
tr = TreeNode(20)
tr.left = TreeNode(15)
tr.right = TreeNode(7)
root.right = tr


a = Solution()
print(a.verticalTraversal(root))

