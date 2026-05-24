# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        dummy = ListNode(0, head)
        left_prev = dummy
        for i in range(left - 1):
            left_prev = left_prev.next

        left_p = left_prev.next

        right_p = head
        for i in range(right - 1):
            right_p = right_p.next

        right_next = right_p.next

        cur = left_p
        prev = None
        while cur and cur != right_next:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        left_prev.next = right_p
        left_p.next = right_next

        return dummy.next