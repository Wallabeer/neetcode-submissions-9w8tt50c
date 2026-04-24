class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        
        result = []
        n = len(digits)
        Map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        text = []
        def helper(i):
            if i == n:
                result.append(''.join(text))
                return
            num = digits[i]
            chars = Map.get(num, '')

            for char in chars:
                text.append(char)
                helper(i+1)
                text.pop()
        
        helper(0)
        return result

            
