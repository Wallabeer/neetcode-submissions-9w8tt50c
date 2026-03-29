class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        left = 0
        charCount={}
        maxCount = 0

        for right in range(len(s)):
            charCount[s[right]] = charCount.get(s[right], 0) + 1
            maxCount = max(maxCount, charCount[s[right]])
            
            while left <= right:
                length = right - left + 1
                replacement = length - maxCount
                if replacement <= k:
                    result = max(result, length)
                    break
                else:
                    charCount[s[left]] = charCount[s[left]] - 1
                    left = left + 1
                    
        return result