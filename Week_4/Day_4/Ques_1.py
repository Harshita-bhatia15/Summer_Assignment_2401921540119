# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, sum):
            if node == None:
                return False

            sum = sum + node.val

            if node.left == None and node.right == None:
                if sum == targetSum:
                    return True

            if dfs(node.left, sum) or dfs(node.right, sum):
                return True

            return False

        return dfs(root, 0)