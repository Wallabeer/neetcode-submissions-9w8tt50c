class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        check = {}

        for index, num in enumerate(nums):
            # print(index, num)
            ref = check.get(num, -1) 
            if ref >= 0:
                return [ref, index]
            else:
                check[target - num] = index

