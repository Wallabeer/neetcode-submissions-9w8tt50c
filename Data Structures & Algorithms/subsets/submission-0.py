class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            # print(num)
            # print(x+[num] for x in result)
            result.extend([x + [num] for x in result])
        return result

    
    
            