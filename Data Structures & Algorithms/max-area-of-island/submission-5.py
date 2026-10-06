class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_len = 0

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        def dfs(row, col):
            directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
            if (row,col) in visited or row < 0 or row == rows or col < 0 or col == cols or grid[row][col] == 0:
                return 0

            visited.add((row, col))
            area = 1
            for dr, dc in directions:
                new_r = row + dr
                new_c = col + dc
                area += dfs(new_r, new_c)
            return area
        
        for r in range(rows):
            for c in range(cols):
                max_len = max(max_len, dfs(r, c))
                
        
        return max_len
