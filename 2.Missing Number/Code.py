class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n = len(nums)
        # expected_sum = n * (n + 1) // 2
        # actual_sum = sum(nums)
        # return expected_sum - actual_sum

        res = len(nums)
        for i in range(len(nums)):
            res ^= i ^ nums[i]
        return res

nums = [3,0,1]
run = Solution()
print(run.missingNumber(nums))