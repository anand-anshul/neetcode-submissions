# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ptr_A = headA
        ptr_B = headB

        while ptr_A != ptr_B:
            if ptr_A:
                ptr_A = ptr_A.next
            else:
                ptr_A = headB
            
            if ptr_B:
                ptr_B = ptr_B.next
            else:
                ptr_B = headA

        return ptr_A