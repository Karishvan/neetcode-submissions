class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Unionfind
        par = [i for i in range(n)]
        rank = [1] * n

        def findPar(n1):
            res = n1

            while par[res] != res:
                par[res] = par[par[res]]
                res = par[res]
            
            return res
        
        def union (n1, n2):
            p1, p2 = findPar(n1), findPar(n2)

            if p1 == p2:
                return 0
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return 1
        components = n
        for (n1, n2) in edges:
            components -= union(n1, n2)
        
        return components

        
        
            
