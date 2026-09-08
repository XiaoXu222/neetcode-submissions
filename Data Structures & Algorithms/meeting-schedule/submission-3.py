"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda pair: pair.start)
        res = True
        if not intervals:
            return True
        prevEnd = intervals[0].end
        

        for i in range(1, len(intervals)):
            if intervals[i].start >= prevEnd:
                prevEnd = intervals[i].end
            else:
                return False
        return res
