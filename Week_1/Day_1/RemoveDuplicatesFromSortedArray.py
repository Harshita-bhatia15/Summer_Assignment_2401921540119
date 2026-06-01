class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        i = 0
        j = i+1
        while(j<n):
            if nums[j] == nums[i]:
                j=j+1
            else:
                i=i+1
                k = nums[i]
                nums[i] = nums[j]
                nums[j] = k
                j=j+1    
        return(i+1)        