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

        # heap = []
        # for key, value in freq.items():
        #     heapq.heappush(heap, (value, key))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        # # print(heap)

        # result = [i[1] for i in heap]
        # return result

        bucket = [[] for i in range(0, len(nums) + 1)]
        for key, value in freq.items():
            bucket[value].append(key)
        print(bucket)

        result = []
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
        