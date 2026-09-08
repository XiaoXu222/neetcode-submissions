class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        sortIntervals = sorted(intervals)
        print(sortIntervals)
        res = [sortIntervals[0]]
        
        for i in range(1, len(sortIntervals)):
            if sortIntervals[i][0] <= res[-1][1]:
                res[-1] = [res[-1][0], max(res[-1][1], sortIntervals[i][1])]
            else:
                res.append(sortIntervals[i])
        return res
        
        

                



        