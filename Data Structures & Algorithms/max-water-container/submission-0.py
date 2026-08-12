class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            res = max(res, area)

            if heights[l] <= heights[r]:
                smaller = heights[l]
                while l < r:
                    l += 1
                    if heights[l] > smaller:
                        break
                if l == r:
                    return res
            elif heights[r] < heights[l]:
                smaller = heights[r]
                while l < r:
                    r -= 1
                    if heights[r] > smaller:
                        break
                if l == r:
                    return res
                
        return res
        