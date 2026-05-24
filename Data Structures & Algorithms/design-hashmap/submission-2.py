class ListNode():
    def __init__(self, key: int) -> None:
        self.key = key
        self.next = None
        self.value = None

class MyHashMap:

    def __init__(self):
        self.hashSet = [ListNode(0) for _ in range(10**4)]

    def put(self, key: int, value: int) -> None:
        idx = key % len(self.hashSet)
        cur = self.hashSet[idx]
        while cur.next:
            if cur.next.key == key:
                cur.next.value = value
                return
            cur = cur.next
        cur.next = ListNode(key)
        cur.next.value = value


    def get(self, key: int) -> int:
        idx = key % len(self.hashSet)
        cur = self.hashSet[idx]
        while cur.next:
            if cur.next.key == key:
                return cur.next.value
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        idx = key % len(self.hashSet)
        cur = self.hashSet[idx]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
