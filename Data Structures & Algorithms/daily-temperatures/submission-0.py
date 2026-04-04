class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        
        for index, temperature in enumerate(temperatures):
            if not stack or temperature < stack[-1][0]:
                stack.append([temperature, index])
            else:
                while stack and stack[-1][0] < temperature:
                    stackTemperatuer, stackIndex = stack.pop()
                    result[stackIndex] = index - stackIndex
                stack.append([temperature, index])
        return result