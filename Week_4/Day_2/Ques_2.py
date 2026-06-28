# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        result = []
        queue = deque([])
        queue.append(root)

        while len(queue) != 0:
            list = []
            length = len(queue)
            for i in range(length):
                current = queue.popleft()
                list.append(current.val)

                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)
            result.append(list)

        return result