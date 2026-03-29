class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
                continue

            if len(stack) == 0:
                return False

            last = stack.pop(-1)
            print(char ,last)
            if char == ')' and last != '(':
                return False
            
            if char == '}' and last != '{':
                return False

            if char == ']' and last != '[':
                return False
        
        if len(stack) > 0:
            return False
        
        return True