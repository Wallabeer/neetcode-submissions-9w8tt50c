class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCount = {}
        for task in tasks:
            taskCount[task] = taskCount.get(task, 0) + 1
        
        import heapq
        from collections import deque
        
        heap = []
        for task, count in taskCount.items():
            heapq.heappush(heap, [-1*count, task])

        print(heap)
        result = 0
        queue = deque()
        meet = len(taskCount)
        while meet > 0:
            if heap:
                count, task = heapq.heappop(heap)
                # print(task)
                if count == -1 and task in taskCount:
                    meet = meet - 1
                queue.append([count + 1, task])
            else:
                # print('idle')
                queue.append([0, 'idle'])
            result += 1

            while len(queue) > n and meet > 0:
                count, task = queue.popleft()
                # print('queue', count, task)
                if count < 0:
                    heapq.heappush(heap, [count, task])
                
        return result
