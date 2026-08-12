class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board)):
                 if board[r][c] != ".":
                    if ((board[r][c] in rows[r]) 
                        or (board[r][c] in cols[c])
                        or (board[r][c] in squares[(r//3, c//3)])):
                        return False

                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    squares[(r//3,c//3)].add(board[r][c])
        
        return True
        
        # for row in board:
        #     sums = [0] * 9
        #     for element in row:
        #         if element != ".":
        #             num = int(element)
        #             sums[num-1] += 1
        #     for sumNum in sums:
        #         if sumNum > 1:
        #             return False

        # for j in range(len(board)):
        #     sums = [0] * 9
        #     for i in range(len(board)):
        #         element = board[i][j]
        #         if element != ".":
        #             num = int(element)
        #             sums[num-1] += 1
        #     for sumNum in sums:
        #         if sumNum > 1:
        #             return False
        
        # sumsGrid = []
        # for i in range(len(board)):
        #     sumsGrid.append([0]*9)

        # for j in range(len(board)):
        #     for i in range(len(board)):
        #         if board[i][j] != ".":
        #             num = int(board[i][j])
        #             sumsGrid[i//3 + (j//3)*3][num-1] += 1
        
        # for row in sumsGrid:
        #     for element in row:
        #         if element > 1:
        #             return False
        
        # return True




                
            



        