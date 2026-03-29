class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left, right = 0, len(s)-1
        
        while left<=right:
            while left < right and self.skip(s[left]):
                left = left + 1

            while left < right and self.skip(s[right]):
                right = right - 1

            if s[left].lower() == s[right].lower():
                left = left + 1
                right = right - 1
            else:
                return False
        return True

    def isValid(self, char):
        if ord('A') <= ord(char) <= ord('Z'):
            return True
        if ord('a') <= ord(char) <= ord('z'):
            return True
        if ord('0') <= ord(char) <= ord('9'):
            return True
        return False

    def skip(self, char):
        return not self.isValid(char)