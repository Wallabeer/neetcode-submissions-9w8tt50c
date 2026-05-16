class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        prevEnd = intervals[0][0]
        count = 0 

        for i in intervals:
            if i[0] < prevEnd:
                print(i)
                count +=1
                prevEnd = min(prevEnd, i[1])
            else:
                prevEnd = i[1]
        return count