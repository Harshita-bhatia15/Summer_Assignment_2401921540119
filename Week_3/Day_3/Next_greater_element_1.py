class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        stack = []

        for j in nums2:
            while len(stack)>0 and stack[-1]<j:
                key = stack.pop()
                hashmap[key] = j
            stack.append(j)

        while len(stack)>0:
            key = stack.pop()
            hashmap[key] = -1
        res = []

        for i in nums1:
            res.append(hashmap[i])
        return res
