class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        cols = set()
        pos_diagonals = set()
        neg_diagonals = set()

        res = []

        def is_valid(r, c):
            if c in cols:
                return False
            # print(diagonal_occupied, r, c)
            pos_code = r + c
            neg_code = r - c
            
            if pos_code in pos_diagonals or neg_code in neg_diagonals:
                return False
            return True


        def backtrack(r):

            # Base Case

            if r == n:
                current_board = []
                for row in board:
                    current_board.append("".join(row))
                res.append(current_board)
                return
            
            for c in range(n):
                if not is_valid(r,c):
                    continue
                
                
                cols.add(c)
                pos_diagonals.add(r+c)
                neg_diagonals.add(r-c)
                board[r][c] = 'Q'
                backtrack(r+1)
                cols.remove(c)
                pos_diagonals.remove(r+c)
                neg_diagonals.remove(r-c)
                board[r][c] = '.'

        
        backtrack(0)
        return res
