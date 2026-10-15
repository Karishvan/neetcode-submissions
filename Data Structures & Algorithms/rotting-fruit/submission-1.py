class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = [-2]
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        fresh_fruit = set()
        def bfs():
            while q:
                res[0] += 1
                print(q)
                print(visited)
                for i in range(len(q)):
                    (r, c) = q.popleft()
                    if r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in visited or grid[r][c] == 0:
                        continue
                    if grid[r][c] == 1:
                        fresh_fruit.remove((r, c))
                    visited.add((r, c))
                    q.append((r + 1, c))
                    q.append((r - 1, c))
                    q.append((r, c - 1))
                    q.append((r, c + 1))
                
                

    
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh_fruit.add((r, c))
        
        bfs()

        return -1 if len(fresh_fruit) != 0 else max(res[0], 0)