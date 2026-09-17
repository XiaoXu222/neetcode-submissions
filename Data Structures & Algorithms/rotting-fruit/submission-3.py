from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        time = 0

        countOne = 0
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    countOne += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))
        
        if countOne == 0:
            return 0
        
        countTurn = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while queue and countTurn < countOne:
            for i in range(len(queue)):
                qr, qc = queue.popleft()
                for dr, dc in directions:
                    nr = qr + dr
                    nc = qc + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        queue.append((nr, nc))
                        grid[nr][nc] = 2
                        countTurn += 1
            time += 1
        
        if countTurn < countOne:
            return -1
        else:
            return time
                    


        