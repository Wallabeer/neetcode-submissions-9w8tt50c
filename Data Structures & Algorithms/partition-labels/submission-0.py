class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cache={}
        n = len(s)
        for i in range(n):
            char = s[i]
            cache[char] = i
        
        result = []
        size = 0
        start = 0
        for i in range(n):
            char = s[i]
            size = max(size, cache[char])
            if size == i:
                result.append(size-start+1)
                start = i+1
                size = 0
        
        return result
            
            