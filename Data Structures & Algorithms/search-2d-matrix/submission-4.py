class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int):
        m = len(matrix)
        n = len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = l + (r - l) // 2
            mid_i = mid // n
            mid_j = mid % n
            if matrix[mid_i][mid_j] < target:
                l = mid + 1
            elif matrix[mid_i][mid_j] > target:
                r = mid - 1
            else:
                return True
        return False

        # m = len(matrix)
        # n = len(matrix[0])
        # l, r = 0, m * n - 1
        # while l <= r:
        #     mid = l + (r - l) // 2
        #     x = mid // n
        #     y = mid % n
        #     if matrix[x][y] < target:
        #         l = mid + 1
        #     elif matrix[x][y] > target:
        #         r = mid - 1
        #     else:
        #         return True
        
        # return False
        