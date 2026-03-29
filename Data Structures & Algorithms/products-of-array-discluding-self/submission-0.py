class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prev = [1] * length
        suff = [1] * length

        for index in range(length):
            if index > 0:
                prev[index] = nums[index - 1] * prev[index - 1]
        for index in range(length, -1, -1):
            if index < length-1:
                suff[index] = nums[index + 1] * suff[index + 1]
        
        # prev[0] = 1
        # suff[-1] = 1
        result = []
        for index in range(length):
            result.append(prev[index] * suff[index])
        
        return result