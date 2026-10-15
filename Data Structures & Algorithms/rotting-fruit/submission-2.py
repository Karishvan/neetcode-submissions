class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        fresh_fruit = 0
          

    
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh_fruit += 1
        
        directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        while q and fresh_fruit > 0:
            for i in range(len(q)):
                (r, c) = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    
                    if (row < 0 or row == ROWS or col < 0 or col == COLS or 
                        grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    q.append((row, col))
                    fresh_fruit -= 1
            res += 1

        return -1 if fresh_fruit > 0 else res