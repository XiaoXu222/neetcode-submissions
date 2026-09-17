from collections import deque

class Solution:
    def numIslands(self, grid) -> int:
        rows, columns = len(grid), len(grid[0])
        directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))

            while queue:
                for i in range(len(queue)):
                    qr, qc = queue.popleft()
                    for dr, dc in directions:
                        if 0 <= qr + dr < rows and 0 <= qc + dc < columns and grid[qr + dr][qc + dc] == "1":
                            queue.append((qr + dr, qc + dc))
                            grid[qr + dr][qc + dc] = "0" 
        
        res = 0
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1":
                    bfs(r, c)
                    res += 1
        return res






        