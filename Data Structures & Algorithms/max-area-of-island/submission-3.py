class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_len = 0

        rows = len(grid)
        cols = len(grid[0])
        global_visited = set()
        visited = set()
        def dfs(row, col):
            directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
            if (row,col) not in visited and 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1:
                visited.add((row, col))
                global_visited.add((row, col))
                for dr, dc in directions:
                    new_r = row + dr
                    new_c = col + dc
                    dfs(new_r, new_c)
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in global_visited:
                    visited = set()
                    dfs(r,c)
                    max_len = max(max_len, len(visited))
                
        
        return max_len
