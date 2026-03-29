class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq

        freq = {}
        for num in nums:
            # if num in freq:
            #     freq[num] = freq[num] + 1
            # else:
            #     freq[num] = 1
            freq[num] = freq.get(num, 0) + 1
        # print(freq)

        heap = []
        for key, value in freq.items():
            heapq.heappush(heap, (value, key))
            if len(heap) > k:
                heapq.heappop(heap)
        # print(heap)

        result = [i[1] for i in heap]
        return result
        