class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = []
        for i in range(len(gas)):
            diff.append(gas[i] - cost[i])
        
        curSum = 0
        index = 0

        for i in range(len(gas)):
            if curSum + diff[i] < 0:
                index = i + 1
                curSum = 0
            else:
                curSum += diff[i]
        
        backSum = 0

        if index < len(gas):
            if sum(diff[:index]) + curSum >= 0:
                return index
            else:
                return -1
        else:
            return -1
        
