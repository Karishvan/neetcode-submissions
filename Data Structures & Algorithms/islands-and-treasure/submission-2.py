class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs(q):
            visited = set()
            current_distance = 0
            while q:
                qlen = len(q)
                for i in range(qlen):
                    (r_next, c_next) = q.popleft()
                    if (r_next, c_next) in visited or r_next < 0 or r_next >= ROWS or c_next < 0 or c_next >= COLS or grid[r_next][c_next] == -1:
                        continue
                    grid[r_next][c_next] = current_distance
                    visited.add((r_next, c_next))
                    q.append((r_next + 1, c_next))
                    q.append((r_next - 1, c_next))
                    q.append((r_next, c_next + 1))
                    q.append((r_next, c_next - 1))
                current_distance += 1
                    

            
            
        q = deque()
        for r in range (ROWS):
            for c in range (COLS):
                if grid [r][c] == 0:
                    q.append((r, c))
        
        bfs(q)



                    
            
       