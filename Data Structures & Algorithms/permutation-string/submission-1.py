class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Char = [0] * 26
        s2Char = [0] * 26
        for i in range(len(s1)):
            index = ord(s1[i]) - ord('a')
            s1Char[index] += 1
            
            index  = ord(s2[i]) - ord('a')
            s2Char[index] += 1

        matches = 0
        for i in range(26):
            if s1Char[i] == s2Char[i]:
                matches += 1
        if matches == 26:
            return True
        
        # print(s1Char)
        # print(matches)
        left = 0 
        for right in range(len(s1), len(s2)):
            index = ord(s2[right]) - ord('a')
            s2Char[index] += 1
            if s2Char[index] == s1Char[index]:
                matches += 1
            if s2Char[index] - 1 == s1Char[index]:
                matches -= 1
            
            index = ord(s2[left]) - ord('a')
            s2Char[index] -= 1
            if s2Char[index] == s1Char[index]:
                matches += 1
            
            if s2Char[index] + 1 == s1Char[index]:
                matches -= 1
            
            # print(matches)
            if matches == 26:
                return True
            left += 1
            
        return False
         