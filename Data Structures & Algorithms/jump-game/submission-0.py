class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)-1
        # print(list(range(len(nums)-2, 0, -1)))
        for i in range(len(nums)-2, -1, -1):
            print(i, n, nums[i])
            if i + nums[i] >= n:
                n = i
                print(n)
        return n == 0

            
            