# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def find_mid(head):
            slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def reverse(head):
            prev = None
            cur = head

            while cur:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            
            return prev

        mid = find_mid(head)
        head2 = reverse(mid)

        cur1 = head
        cur2 = head2

        highest = float('-inf')
        while cur2:
            cur_sum = cur1.val + cur2.val
            highest = max(highest, cur_sum)
            cur1 = cur1.next
            cur2 = cur2.next

        return highest
