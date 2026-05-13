"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        result = 0
        start = [i.start for i in intervals]
        start.sort()
        end = [i.end for i in intervals]
        end.sort()

        n = len(intervals)        
        s = 0
        e = 0
        count = 0
        while s < n:
            if start[s] < end[e]:
                count += 1
                s += 1
                result = max(result, count)
            else:
                count -= 1
                e += 1
        return result