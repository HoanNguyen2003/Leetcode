class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # Dict = {}
        # for i in range(len(nums)):
        #     Dict[nums[i]] = Dict.get(nums[i], 0) + 1
        
        # sorted_items = sorted(Dict.items(), key=lambda x: x[1], reverse=True)
        # return([item[0] for item in sorted_items[:k]])

        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        n = len(nums)
        buckets = [[] for _ in range(n + 1)]

        for num, freq in freq_map.items():
            buckets[freq].append(num)
        
        result = []
        for freq in range(n, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]