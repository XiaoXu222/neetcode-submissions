class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sortIntervals = sorted(intervals)
        nonOverlap = [sortIntervals[0]]

        for i in range(1, len(sortIntervals)):
            if sortIntervals[i][0] < nonOverlap[-1][1]:
                if nonOverlap[-1][1] > sortIntervals[i][1]:
                    nonOverlap[-1] = sortIntervals[i]
            else:
                nonOverlap.append(sortIntervals[i])
        return len(sortIntervals) - len(nonOverlap) 



        