class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        hashset = set(nums)
        result = 1
        for num in nums:
            if num - 1 not in hashset:
                count = 1
                while num + count in hashset:
                    count = count + 1
                result = max(result, count)

        return result