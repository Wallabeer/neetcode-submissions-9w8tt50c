class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        n = len(nums)
        permutation = []
        choosen = [False] * n
        def helper():
            if len(permutation) == n:
                result.append(permutation.copy())
                return
            
            for index, val in enumerate(choosen):
                if val:
                    continue
                if not val:
                    permutation.append(nums[index])
                    choosen[index] = True
                    helper()
                
                permutation.pop()
                choosen[index] = False
        helper()
        
        return result
            
            