class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCounter = {}
        for char in t:
            tCounter[char] = tCounter.get(char, 0) + 1
        
        result = ''
        resultLength=len(s)
        tLength = len(t)
        left = 0
        right = 0
        # for right in range(len(s)):
        while right < len(s):
            if left < len(s) and s[left] not in tCounter:
                # print('skip', left, right)
                left = left + 1
                right = max(left, right)
                continue

            if s[right] in tCounter:
                tCounter[s[right]] = tCounter.get(s[right]) - 1
            print(left, right, tCounter)
            
            # print(tCounter.items())
            for value in tCounter.values():
                flag = value
                if value > 0:
                    right = right + 1
                    break
            if flag > 0:
                continue
            
            length = right - left + 1
            if length <= resultLength:
                result = s[left:right + 1]
                resultLength = length
                print(left, s[left], right, s[right], result, resultLength)
            # print(tCounter[s[left]])
            if s[left] in tCounter:
                tCounter[s[left]]=tCounter.get(s[left]) + 1
            if s[right] in tCounter:
                tCounter[s[right]] = tCounter.get(s[right]) + 1
            left = left + 1
        return result



