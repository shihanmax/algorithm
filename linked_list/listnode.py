# 链表类
class listNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def printMe(self):
        curr = self
        while curr:
            print(curr.val, end='->')
            curr = curr.next
        print('NULL')


if __name__ == '__main__':
    head = listNode(3)
    head.next = listNode(6)
    head.next.next = listNode(9)
    head.next.next.next = listNode(12)
    head.printMe()