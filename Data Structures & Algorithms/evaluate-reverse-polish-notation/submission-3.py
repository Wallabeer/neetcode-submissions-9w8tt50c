class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        token = tokens.pop()
        if token not in '+-*/':
            return int(token)

        b = self.evalRPN(tokens)
        a = self.evalRPN(tokens)
        if token == '+':
            num = a + b
        if token == '-':
            num = a - b
        if token == '*':
            num = a * b
        if token == '/':
            num = int(a / b)
        return num
                     