class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]

        def union(node1, node2):
            parent[find(node1)] = find(node2)

        def find(node1):
            while parent[node1] != node1:
                node1 = parent[node1]
            
            return node1
                
        
        #populate parents

        for (node1, node2) in edges:
            union(node1, node2)

        res = 0
        for i in range(len(parent)):
            if parent[i] == i:
                res += 1
        
        return res