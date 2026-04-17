class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        sumi = 0
        n = len(candidates)
        solution = []
        def helper(sumi, i):
            if sumi == target:
                result.append(solution.copy())
                return
            
            if sumi > target:
                return
            if i >= n:
                return

            num = candidates[i]
            
            solution.append(num)
            helper(sumi+ num, i+1)

            solution.pop()
            skip = 0
            while i+1+skip < n and num == candidates[i+1+skip]:
                skip += 1
            helper(sumi, i+1+skip)

        helper(0, 0)
        return result