class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # new = []
        # n = len(nums)
        # for i in range(n):
        #     new.append(i+1)
        # for i in range(n):
        #     if nums[i] in new:
        #         new.remove(nums[i])
        # return new
            
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])

        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)

        return result

nums = [4,3,2,7,8,2,3,1]
run = Solution()
print(run.findDisappearedNumbers(nums))