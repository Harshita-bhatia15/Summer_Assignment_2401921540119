class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        maxArea = float("-inf")
        while left<right:
            area = min(height[left],height[right])*(right-left)
            maxArea = max(maxArea,area)
            if (height[left]<height[right]):
                left = left+1
            else:
                right = right-1
        return maxArea

