class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.tail = Node(-1, -1)
        self.head = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_tail(self, node: Node):
        prev_node = self.tail.prev
        node.prev = prev_node
        node.next = self.tail
        prev_node.next = node
        self.tail.prev = node

    def remove_node(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1

        node = self.hashmap[key]
        self.remove_node(node)
        self.add_to_tail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.remove_node(node)
            del self.hashmap[key]

        node = Node(key, value)
        self.hashmap[key] = node
        self.add_to_tail(node)

        if len(self.hashmap) > self.capacity:
            lru_node = self.head.next
            self.remove_node(lru_node)
            del self.hashmap[lru_node.key]