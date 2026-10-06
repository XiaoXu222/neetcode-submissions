class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        def dfs(r, c):
            if min(r, c) < 0 or r == row or c == col or grid[r][c] == "0":
                return 
            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        res = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
        return res
        
