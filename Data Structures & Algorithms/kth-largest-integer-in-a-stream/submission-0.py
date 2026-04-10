class KthLargest:
    import heapq
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        self.helper()
        
    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        self.helper()
        return self.nums[0]

    def helper(self):
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)