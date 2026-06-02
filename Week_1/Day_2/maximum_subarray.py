class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        sum = 0

        max = float("-inf")
        for i in range(0,n):
            sum = sum+nums[i]
            if sum>max:
                max = sum
            if sum<0:
                sum = 0
        return max        