# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0

            leftH = height(node.left)
            rightH = height(node.right)

            return 1 + max(leftH, rightH)

        if not root:
            return True

        leftH = height(root.left)
        rightH = height(root.right)

        diff = abs(leftH - rightH)

        if diff > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)


