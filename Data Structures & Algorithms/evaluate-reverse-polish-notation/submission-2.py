class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for token in tokens:
            
            if token not in '+-*/':
                nums.append(int(token))
            else:
                b = nums.pop()
                a = nums.pop()

                if token == '+':
                    num = a + b
                if token == '-':
                    num = a - b
                if token == '*':
                    num = a * b
                if token == '/':
                    num = int(a / b)
                nums.append(num)
            
        return nums[0]