class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(head):
            prev = None
            cur = head
            while cur:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            return prev

        def middle(head):
            fast = head
            slow = head

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        middle_node = middle(head)
        second_head = reverse(middle_node)

        left, right = head, second_head

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True