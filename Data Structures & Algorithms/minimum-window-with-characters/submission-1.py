class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '':
            return ''
        
        tCounter = {}
        for char in t:
            tCounter[char] = tCounter.get(char, 0) + 1
        
        tLength = len(t)
        sLength = len(s)

        result = [0, 0]
        resultLength=sLength + 1
        condition = len(tCounter)
        meet = 0

        left = 0
        while left < sLength and s[left] not in tCounter :
            left = left + 1
        for right in range(left, sLength):
            char = s[right]

            if char in tCounter:
                tCounter[char] = tCounter[char] - 1
                if tCounter[char] == 0:
                    meet = meet + 1
                    
            print(meet, condition)

            while meet == condition:
                # print('v', meet, condition)
                print('v', s[left: right+1]) 
                length = right - left + 1
                if length < resultLength:
                    result = [left, right]
                    resultLength = length                    
                    
                charLeft = s[left]
                tCounter[charLeft] = tCounter[charLeft] + 1
                if tCounter[charLeft] == 1:
                    meet = meet - 1
                    
                left = left + 1
                while left < sLength and s[left] not in tCounter:
                    left = left + 1
                    print('x', meet, left, right, s[left:right+1])
            print('X--' , meet, left, right, s[left:right+1])
        print(result)
        left, right = result
        
        if resultLength <= sLength:
            return s[left:right+ 1]
        else:
            return ''