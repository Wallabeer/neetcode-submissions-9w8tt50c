class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        # n = len(nums)

        maxi = 1
        mini = 1
        
        for num in nums:
            temp = maxi
            maxi = max(num, num * maxi, num * mini)
            mini = min(num, num * temp, num * mini)
            result = max(maxi, result)
            print(maxi, mini)
        
        return result