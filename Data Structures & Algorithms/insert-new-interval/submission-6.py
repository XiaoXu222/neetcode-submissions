class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        # if not intervals:
        #     return [newInterval]
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                # res.append(intervals[i:])
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
                # if i == len(intervals) - 1:
                #     res.append(newInterval)
                #     return res
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
                # if i == len(intervals) - 1:
                #     res.append(newInterval)
                #     return res
        res.append(newInterval)
        return res
                
                    
        




        