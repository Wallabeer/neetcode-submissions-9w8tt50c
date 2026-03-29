class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        hashset = set(nums)
        result = 1
        for num in nums:
            if num - 1 not in hashset:
                count = 1
                pointer = num + 1
                while True:
                    if pointer in hashset:
                        count = count + 1
                        pointer = pointer + 1
                        result = max(result, count)
                    else:
                        break
        return result