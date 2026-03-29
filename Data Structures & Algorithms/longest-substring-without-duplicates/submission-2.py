class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        start = 0
        end = 0
        charSet = set()

        while end < len(s):
            if s[end] in charSet:
                charSet.remove(s[start])
                start = start + 1
            else:
                result = max(result, end - start + 1)
                charSet.add(s[end])
                end = end + 1
            
        return result