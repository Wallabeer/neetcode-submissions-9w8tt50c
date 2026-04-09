class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        maxi = max(piles)
        result = maxi

        left = 1
        right = maxi
        while left <= right:
            mid = (left + right) // 2
            # print(left, right, mid)

            time = 0
            for pile in piles:
                time += math.ceil(pile/mid)
            print(time)
            if time <= h:
                result = min(result, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return result
            