class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        indexMap = {}
        for i, val in enumerate(s):
            indexMap[val] = i

        l, r = 0, 0
        res = []
        for i, val in enumerate(s):
            r = max(r, indexMap[val])
            if i == r:
                res.append(r - l + 1)
                l = r + 1
           
        return res
            