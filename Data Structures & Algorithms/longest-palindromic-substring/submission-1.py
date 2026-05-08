class Solution:
    def longestPalindrome(self, s: str) -> str:
        resultStart = 0
        resultLen = 0
        
        n = len(s)
        for i in range(n):
            left = i
            right = i
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > resultLen:
                    print(i)
                    resultLen = right - left + 1
                    resultStart = left
                
                left -= 1
                right += 1
            

            if i+1 < n and s[i] == s[i+1]:
                left = i
                right = i+1
                while left >= 0 and right < n and s[left] == s[right]:
                    if right - left + 1 > resultLen:
                        print('--',i)
                        resultLen = right - left + 1
                        resultStart = left
                    
                    left -= 1
                    right += 1

        return s[resultStart:resultStart+resultLen]
