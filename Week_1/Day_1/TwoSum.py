class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        n = len(nums)
        for i in range(0,n):
            m = target - nums[i]
            if m in hashmap:
                return(hashmap[m], i)
            else:
                hashmap[nums[i]] = i    
                