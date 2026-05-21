class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        
        k = k % length
        if k == 0:
            return head

        fwd = head
        while k > 0:
            fwd = fwd.next
            k -= 1
        
        cur = head

        while fwd.next:
            cur = cur.next
            fwd = fwd.next

        new_head = cur.next
        fwd.next = head
        cur.next = None
        
        return new_head