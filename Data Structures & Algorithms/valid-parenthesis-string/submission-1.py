class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        stack1 = []
        stack2 = []

        print(n)
        for i in range(n):
            print(i)
            char = s[i]
            print(char)
            if char == '(':
                stack1.append(i)
            
            if char == '*':
                print(char)
                stack2.append(i)
            
            if char == ')':
                if stack1:
                    stack1.pop()
                elif stack2:
                    stack2.pop()
                else:
                    return False
            
        print(stack1)
        print(stack2)

        while stack1 and stack2:
            if stack1.pop() > stack2.pop():
                return False
            
        if stack1:
            return False
        else:
            return True
