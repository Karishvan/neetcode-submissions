class Solution:
    def solve(self, board: List[List[str]]) -> None:
        region = set()
        ROWS = len(board)
        COLS = len(board[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        def bfs(i, j):
            logging = False
            q = deque()
            q.append((i, j))
            while q:
                for i in range(len(q)):
                    (r, c) = q.popleft()
                    for dr, dc in directions:
                        row, col = r + dr, c + dc
                        if (row < 0 or row >= ROWS or
                            col < 0 or col >= COLS):
                            return False
                        if (row, col) in region or board[row][col] == 'X':
                            continue
                        
                        region.add((row, col))
                        q.append((row, col))
            for r, c in region:
                board[r][c] = 'X'
            # print(board)
                        
                        
                        
                        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    region.add((i, j))
                    bfs(i, j)
                    region = set()
        
        
                    

