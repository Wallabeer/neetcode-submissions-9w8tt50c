class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        result = float('-inf')
        pointer = 0

        runningSum = 0
        while pointer < n:
            if runningSum < 0:
                runningSum = nums[pointer]
            else:
                runningSum += nums[pointer]
            print(result, runningSum) 
            result = max(result, runningSum)
            pointer += 1
        return result
            
        