class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        n = len(nums)
        for i in range(0,n):
            if nums[i] in hashmap:
                return True
                break
            else:
                hashmap[nums[i]] = 0
        return False           