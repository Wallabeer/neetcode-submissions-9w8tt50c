class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        
        n = len(nums)
        solution = []
        sumi = 0
        def helper(sumi, i):
            if sumi == target:
                result.append(solution.copy())
                return
            if i >= n:
                return
            if sumi > target:
                return 
            
            num = nums[i]
            solution.append(num)
            sumi += num
            helper(sumi, i)
            
            solution.pop()
            sumi -= num
            helper(sumi, i+1)
    
        helper(0, 0)
        return result