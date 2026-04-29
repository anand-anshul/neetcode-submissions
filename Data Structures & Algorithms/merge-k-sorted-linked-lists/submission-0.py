# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        def merge2(l1, l2):
            dummy = ListNode()
            cur = dummy

            while l1 and l2:
                if l1.val <= l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next

            if l1:
                cur.next = l1
            if l2:
                cur.next = l2

            return dummy.next

        for i in range(1, len(lists)):
            lists[i] = merge2(lists[i], lists[i - 1])

        return lists[-1]
