class Solution(object):
    def maxArea(height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 1:
            return 0

        start = 0
        end = len(height) - 1
        vol = 0

        while start < end:
            if height[start] < height[end]:
                vol = max(min(height[end],height[start]) * (end - start), vol)
                start += 1
            else:
                vol = max(min(height[start],height[end]) * (end - start), vol)
                end -= 1
        return vol
        
    # Test case
    height = [1,8,6,2,5,4,8,3,7]
    result = maxArea(height)
    print(result)