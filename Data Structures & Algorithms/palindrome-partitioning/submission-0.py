class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        n = len(s)
        partition = []
        def helper(i, j):
            if j >= n:
                if j == i:
                    result.append(partition.copy())
                return
            
            if self.isValid(s[i:j+1]):
                partition.append(s[i:j+1])
                helper(j+1, j+1)
                partition.pop()
            helper(i, j+1)
        
        helper(0, 0)
        return result
    
    def isValid(self, s):
        left = 0
        right = len(s) - 1

        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True
    
