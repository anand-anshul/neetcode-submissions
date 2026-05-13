# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        def remove(prev):
            prev.next = prev.next.next

        cur = dummy
        while cur and cur.next:
            if cur.next.val == val:
                remove(cur)
            else:
                cur = cur.next
        return dummy.next