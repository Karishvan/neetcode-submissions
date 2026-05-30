class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        res = []
        pac, atl = set(), set()
        
        def dfs(cell, prev_val, visited):
            (r, c) = cell
            if r == ROWS or c == COLS or heights[r][c] < prev_val or r < 0 or c < 0 or (r,c) in visited:
                return
            
            
           
            visited.add((r, c))
            
            for (dx, dy) in directions:
                new_r, new_c = r + dx, c + dy
                if (new_r, new_c) not in visited:
                    dfs((new_r, new_c), heights[r][c], visited)
            
        # for i in range(ROWS):
        #     for j in range(COLS):
        #         if i == 0 or j == 0:
        #             #print(i, j)
        #             dfs((i, j), heights[i][j], atl)
        #         if i == ROWS-1 or j == COLS-1:
        #             #print(i, j)
        #             dfs((i, j), heights[i][j], pac)
        for r in range(ROWS):
            dfs((r, 0), heights[r][0], pac)
            dfs((r, COLS-1), heights[r][COLS-1], atl)
        for c in range (COLS):
            dfs((0, c), heights[0][c], pac)
            dfs((ROWS-1, c), heights[ROWS-1][c], atl)
        # print(atl)
        # print(pac)
        for i in range (ROWS):
            for j in range(COLS):
                if (i, j) in atl and (i, j) in pac:
                    res.append([i, j])
        return res
                    
                

