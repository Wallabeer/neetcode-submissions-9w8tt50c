class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        result = []

        n = len(intervals)
        pt1 = 0
        pt2 = 1
        while pt2 < n:
            interval1 = intervals[pt1]
            interval2 = intervals[pt2]

            if interval1[1] >= interval2[0]:
                intervals[pt2] = [interval1[0], max(interval1[1], interval2[1])]
            else:
                result.append(interval1)
            
            pt1 += 1
            pt2 += 1
        
        result.append(intervals[pt1])

        return result
