class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # for i in range(len(nums)):
        #     for j in range(1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return i, j

        lookup = {}
        for i, num in enumerate(nums):
            complement = target - num 
            if complement in lookup:
                return(lookup[complement], i)
            lookup[num] = i            
        return(lookup)
        
nums = [2,7,11,15]
target = 9
run = Solution()
print(run.twoSum(nums,target))