class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, tmp in enumerate(temperatures):
            while stack and tmp > stack[-1][0]:
                resTmp, resInd = stack.pop()
                res[resInd] = i - resInd
            stack.append((tmp, i))
        
        return res

        