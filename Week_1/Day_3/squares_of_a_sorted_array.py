class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        while i<n:
            nums[i] = nums[i]**2
            i = i+1
        nums.sort()
        return nums