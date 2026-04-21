class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        nums.sort()
        n = len(nums)
        print(nums)

        subset = []
        def helper(i):
            if i > n-1:
                return
            num = nums[i]
            subset.append(num)
            print(i, subset)
            result.append(subset.copy())
            # print(result)
            helper(i+1)
            
            print('BbbbbbB', i, num)
            subset.pop()
            i += 1
            while i < n and nums[i] == num:
                i += 1
            print('BB',i)
            helper(i)

        helper(0)
        return result
            