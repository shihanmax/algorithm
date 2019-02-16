from listnode import listNode

"""
将单链表反转:
        3 -> 6 -> 9 -> 12 ->NULL
        ==>
NULL <- 3 <- 6 <- 9 <- 12


还需要再研究
"""

def reverseLinkedList(head):
    pre = None
    cur = head
    while cur != None:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next

    return pre


head = listNode(3)
head.next = listNode(6)
head.next.next = listNode(9)
head.next.next.next = listNode(12)

head.printMe()
reverseLinkedList(head).printMe()