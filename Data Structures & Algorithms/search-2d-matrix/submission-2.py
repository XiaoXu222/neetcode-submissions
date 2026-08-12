class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = l + (r - l) // 2
            x = mid // n
            y = mid % n
            if matrix[x][y] < target:
                l = mid + 1
            elif matrix[x][y] > target:
                r = mid - 1
            else:
                return True
        
        return False
        