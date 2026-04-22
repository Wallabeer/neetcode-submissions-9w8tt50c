class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        instance = []
        def helper(openNum=n, closeNum=n):
            if openNum > closeNum:
                return
            
            if openNum == 0 and closeNum == 0:
                result.append(''.join(instance))
                print('******')
                return
            
            if openNum > 0:
                instance.append('(')
                print('11',instance)
                helper(openNum-1, closeNum)
                instance.pop()

            if closeNum > openNum:
                instance.append(')')
                print('22',instance)
                helper(openNum, closeNum-1)
                instance.pop()
            




        helper()
        return result



