class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [n for n in range(len(edges))]
        rank = [0] * len(edges)
        # [1, 2, 3, 4]
        def union(n1, n2):
            rep_n1 = find(n1)
            rep_n2 = find(n2)
            if rep_n1 == rep_n2:
                return False
            if rank[rep_n1] > rank[rep_n2]:
                parent[rep_n2] = rep_n1
                rank[rep_n2] += rank[rep_n1]
            else:
                parent[rep_n1] = rep_n2
                rank[rep_n1] += rank[rep_n2]
            return True
        
        def find(n1):
            if n1 != parent[n1]:
                parent[n1] = find(parent[n1])
            return parent[n1]
        
        for inc, out in edges:
            if not union(inc-1, out-1):
                return [inc, out]
        
        return [inc, out]
        





        

            
