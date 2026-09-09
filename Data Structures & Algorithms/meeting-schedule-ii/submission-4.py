"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        timeLine = []
        for i in range(len(intervals)):
            timeLine.append([intervals[i].start, 1])
            timeLine.append([intervals[i].end, -1])

        timeLine.sort()

        currRooms = 0
        res = 0
        for j in range(len(timeLine)):
            currRooms += timeLine[j][1]
            res = max(res, currRooms)
        return res
        


        