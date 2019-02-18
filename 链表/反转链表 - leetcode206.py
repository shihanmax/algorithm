from listnode import listNode

"""
将单链表反转:
        3 -> 6 -> 9 -> 12 ->NULL
        ==>
NULL <- 3 <- 6 <- 9 <- 12


还需要再研究
"""

def reverseLinkedList(head):
    pPrev = None
    pCurr = head
    while pCurr != None:
        pNext = pCurr.next
        pCurr.next = pPrev
        pPrev = pCurr
        pCurr = pNext

    return pPrev


head = listNode(3)
head.next = listNode(6)
head.next.next = listNode(9)
head.next.next.next = listNode(12)

head.printMe()
reverseLinkedList(head).printMe()
"""
//c++ 
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* pPrev = NULL;
        ListNode* pCurr = head;
        ListNode* pNext = NULL;
        
        while (pCurr) {
            pNext = pCurr->next;
            pCurr->next = pPrev;
            pPrev = pCurr;
            pCurr = pNext;
        }
        
        return pPrev;
    }
};
"""