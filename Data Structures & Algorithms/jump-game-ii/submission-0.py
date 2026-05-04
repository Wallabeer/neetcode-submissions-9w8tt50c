class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)-1
        result = 0
        
        left = 0
        right = 0
        Farthest = 0
        while right < n:
            for i in range(left, right+1):
                Farthest = max(Farthest, nums[i]+ i)
            left = right + 1
            right = Farthest
            result +=1
        
        return result
            


        