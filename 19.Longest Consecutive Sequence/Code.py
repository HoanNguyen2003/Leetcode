class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        num_set = set(nums)
        print(num_set)
        longest = 0

        for num in num_set:
            print("num: ",num)
            if num - 1 not in num_set:  # Kiểm tra điểm bắt đầu chuỗi
                current = num
                streak = 1

                while current + 1 in num_set:
                    current += 1
                    streak += 1

                longest = max(longest, streak)

        return longest

# Input: nums = [100,4,200,1,3,2]
# Output: 4