# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
class Solution:
    def numIslands(self, grid) -> int:
        row, column = len(grid), len(grid[0])
        direction = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        def dfs(r, c):
            if r < 0 or c < 0 or r >= row or c >= column or grid[r][c] == "0":
                return 
            grid[r][c] = "0"
            for dr, dc in direction:
                dfs(r + dr, c + dc)

        res = 0
        for r in range(row):
            for c in range(column):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
        return res

        