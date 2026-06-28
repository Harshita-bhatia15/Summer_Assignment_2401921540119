# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        res = []
        queue = deque([])
        queue.append(root)

        while len(queue) != 0:
            list = []
            length = len(queue)

            for i in range(length):
                curr = queue.popleft()
                list.append(curr.val)

                if curr.left is not None:
                    queue.append(curr.left)

                if curr.right is not None:
                    queue.append(curr.right)

            if len(res) % 2 == 1:
                list.reverse()

            res.append(list)

        return res