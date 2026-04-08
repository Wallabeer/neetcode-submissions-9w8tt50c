class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from heapq import heapify, heappush, heappop
        result = []
        heap = []
        heapify(heap)
        for index, num in enumerate(nums):
            heappush(heap, [-1 * num, index])
            # print(index, heap)
            while len(heap) > k and index - heap[0][1] >= k:
                heappop(heap)
            if len(heap) >= k:
                heapNum, heapIndex = heap[0]
                result.append(-1 * heapNum)
                # print(index ,result)

        return result               
                



