# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        leftmost = rightmost = 0
        col_map = defaultdict(list)

        q = deque([(root, 0)])
        while q:
            level_size = len(q)
            for i in range(level_size):
                node, col_id = q.popleft()
                if node:
                    col_map[col_id].append(node.val)
                if node.left:
                    q.append((node.left, col_id - 1))
                if node.right:
                    q.append((node.right, col_id + 1))
                leftmost = min(leftmost, col_id)
                rightmost = max(rightmost, col_id)
        
        res = []
        for i in range(leftmost, rightmost + 1):
            arr = col_map[i]
            res.append(arr)
        return res

