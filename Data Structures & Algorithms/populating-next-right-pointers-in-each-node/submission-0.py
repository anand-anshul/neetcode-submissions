class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        q = deque([root])

        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if i < size - 1:
                    node.next = q[0]
                else:
                    node.next = None
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root