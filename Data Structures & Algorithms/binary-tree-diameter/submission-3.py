# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftH = self.height(root.left)
        rightH = self.height(root.right)

        diameter = leftH + rightH

        sub = max(
            self.diameterOfBinaryTree(root.left),
            self.diameterOfBinaryTree(root.right)
        )
        return max(diameter, sub)
    


    def height(self, node):
            if not node:
                return 0
            leftH = self.height(node.left)
            rightH = self.height(node.right)

            return 1 + max(leftH, rightH)

        

        