class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        heap = []
        for point in points:
            heapq.heappush(heap, [self.helper(point), point])

            while len(heap) > k:
                heapq.heappop(heap)
        
        return [x[1] for x in heap]

    
    def helper(self, point):
        return -1 *(point[0] ** 2 + point[1] ** 2)