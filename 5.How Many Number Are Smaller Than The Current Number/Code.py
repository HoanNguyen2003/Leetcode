class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # result = []
        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(len(nums)):
        #         if nums[j] < nums[i]:
        #             count+=1
        #     result.append(count)
        # return result    
        
        sorted_nums = sorted(nums)
        count = {}
        for i, num in enumerate(sorted_nums):
            if num not in count:
                count[num] = i
        return([count[num] for num in nums])

nums = [8,1,2,2,3]
run = Solution()
print(run.smallerNumbersThanCurrent(nums))