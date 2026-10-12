class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n
        
        def union(node1, node2):
            p1, p2 = find(node1), find (node2)
            if p1 == p2:
                return False
            if rank[p1] < rank[p2]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return True

        def find(node1):
            current = node1
            while parent[current] != current:
                parent[current] = parent[parent[current]]
                current = parent[current]
            
            return current
                
        
        #populate parents
        res = n

        for (node1, node2) in edges:
            if union(node1, node2):
                res -= 1

        return res

        # Time: O (N + E)
        # Space: O (N)