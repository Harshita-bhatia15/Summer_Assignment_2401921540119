# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = [root.val]

        def solve(node):
            if node == None:
                return 0

            left = solve(node.left)
            right = solve(node.right)

            if left < 0:
                left = 0
            if right < 0:
                right = 0

            maxSum = node.val + left + right

            if result[0] < maxSum:
                result[0] = maxSum

            return node.val + max(left, right)

        solve(root)
        return result[0]
        