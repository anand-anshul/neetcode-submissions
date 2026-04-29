# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(node, a, b):
            if not node or not a or not b:
                return None
            
            if max(a.val, b.val) < node.val:
                return dfs(node.left, a, b)
            elif min(a.val, b.val) > node.val:
                return dfs(node.right, a, b)
            else:
                return node

        return dfs(root, p, q)