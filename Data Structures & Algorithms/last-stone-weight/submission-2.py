class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        stones = [-1 * x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
             stone1 = heapq.heappop(stones)
             stone2 = heapq.heappop(stones)

             if (stone1-stone2) != 0:
                heapq.heappush(stones, stone1-stone2)
        # print(stones)
        return stones[0] * -1 if len(stones) else 0
