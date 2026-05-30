class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()

        adj_list = {i:[] for i in range(n)}
        
        for (u, v) in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            if adj_list[node] == []:
                return True
            for connection in adj_list[node]:
                dfs(connection)
            return True
        res = 0
        for i in range(n):
            if dfs(i):
                res += 1
        
        return res
            
