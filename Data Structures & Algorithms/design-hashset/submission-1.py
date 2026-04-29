class Node:
    def __init__(self, val=None, next=None) -> None:
        self.val = val
        self.next = next

class MyHashSet:

    def __init__(self):
        self.dummy = Node(0)

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        current = self.dummy
        while current.next:
            current = current.next
        node = Node(key)
        current.next = node

    def remove(self, key: int) -> None:
        current = self.dummy.next
        prev = self.dummy
        while current:
            if current.val == key:
                prev.next = current.next
                return
            prev = current
            current = current.next
        

    def contains(self, key: int) -> bool:
        current = self.dummy.next

        while current is not None:
            if current.val == key:
                return True
            current = current.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)