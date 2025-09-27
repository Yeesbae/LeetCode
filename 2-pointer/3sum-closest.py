class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return []

        nums.sort()
        closest_sum = float('inf')

        for i in range(len(nums)):
            start = i + 1
            end = len(nums) - 1
            while start < end:
                total = nums[i] + nums[start] + nums[end]
                if abs(target - total) < abs(target - closest_sum):
                    closest_sum = total
                if total < target:
                    start += 1
                elif total > target:
                    end -= 1
                else:
                    return total
        return closest_sum
                
    # Test case
    nums = [-1, 2, 1, -4]
    target = 1
    result = threeSumClosest(nums, target)
    print(result)