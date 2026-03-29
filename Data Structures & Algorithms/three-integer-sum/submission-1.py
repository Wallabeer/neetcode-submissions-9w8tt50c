class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        # print(nums)

        for index, value in enumerate(nums):
            if value > 0:
                break
            
            if index > 0 and value == nums[index-1]:
                continue
            print(index, value)
            left = index + 1
            right = len(nums) - 1

            while left < right:
                threeSum = value + nums[left] + nums[right]
                
                if threeSum > 0:
                    right = right - 1
                elif threeSum < 0:
                    left = left + 1
                else:
                    result.append([value, nums[left], nums[right]])
                    
                    left = left + 1
                    while left < right and nums[left] == nums[left - 1]:
                        left = left + 1
            # print(result)
        return result