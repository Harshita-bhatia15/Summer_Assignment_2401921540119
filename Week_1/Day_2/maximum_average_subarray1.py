class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0
        for i in range(0,k):
            sum = sum+nums[i]
        
        maxSum = sum
        m = 0
        n = k-1
        while(n<len(nums)-1):
            n = n+1
            sum = sum-nums[m]+nums[n]
            m = m+1
            maxSum = max(maxSum, sum)
        return maxSum/k