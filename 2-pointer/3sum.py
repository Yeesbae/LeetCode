class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) < 3:
            return []
        if len(nums) == 3:
            total = nums[0] + nums[1] + nums[2]
            if total == 0:
                return [nums]
            else:
                return []

        result = []
        nums.sort()
        
        for i in range(len(nums)):
            start = i + 1
            end = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            else :
                while start < end:
                    total = nums[i] + nums[start] + nums[end]
                    if total == 0:
                        result.append([nums[i], nums[start], nums[end]])

                        start += 1
                        end -= 1

                        while start < end and nums[start] == nums[start - 1]:
                            start += 1
                        while start < end and nums[end] == nums[end + 1]:
                            end -= 1
                    elif total < 0:
                        start += 1
                    else:
                        end -= 1
        return result
        

    # Test case
    nums = [-1,0,1,2,-1,-4]
    result = threeSum(nums)
    print(result)