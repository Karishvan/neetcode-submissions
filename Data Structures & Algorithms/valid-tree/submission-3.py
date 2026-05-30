class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = {i:[] for i in range(n)}
        visited = set()

        for (incoming, outgoing) in edges:
            adj_list[incoming].append(outgoing)
            adj_list[outgoing].append(incoming)
        
        def dfs(node, prev_val):
            print(node)
            if node in visited:
                #print("ALREADY VISITED, RETURNING FALSE", node)
                return False
            visited.add(node)
            if adj_list[node] == []:
                return True
            
            for connection in adj_list[node]:
                if not connection == prev_val:
                    if not dfs(connection, node):
                        return False
            return True
        #print(adj_list)
        for i in range(n):
            visited = set()
            #print("STARTING WITH ",i)
            if not dfs(i, -1):
                #print("RETURNED FALSE FOR ", i)
                return False
            if len(visited) == n:
                return True
        
        return False
            
            
