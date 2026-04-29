class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.dummy = ListNode()

    def put(self, key: int, value: int) -> None:
        current = self.dummy.next
        while current:
            if current.val[0] == key:
                current.val = [key, value]
                return
            current = current.next
        
        last = self.dummy
        while last.next:
            last = last.next
        last.next = ListNode([key, value])

    def get(self, key: int) -> int:
        current = self.dummy.next
        while current:
            if current.val[0] == key:
                return current.val[1]
            current = current.next
        return -1

    def remove(self, key: int) -> None:
        current = self.dummy.next
        prev = self.dummy
        while current:
            if current.val[0] == key:
                prev.next = current.next
                return
            prev = current
            current = current.next