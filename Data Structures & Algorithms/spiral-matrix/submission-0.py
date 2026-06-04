class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r, t, b = 0, len(matrix[0])-1, 0 , len(matrix)-1
        visited = set()
        res = []
        print(r)
        while l <= r and t <= b:
            for i in range(l, r+1):
                # Go left to right (top)
                
                if (t,i) not in visited:
                    res.append(matrix[t][i])
                visited.add((t,i))
            print(res)
            print(t+1, b+1)
            for j in range(t+1, b+1):
                # Go top to bottom (right)
                if (j, r) not in visited:
                    res.append(matrix[j][r])
                visited.add((j, r))
            print(res)
            print(r-1, l-1)
            for k in range(r-1, l-1, -1):
                # Go right to left (bottom)
                if (b, k) not in visited:
                    res.append(matrix[b][k])
                visited.add((b, k))
            print(res, "HI")
            for i in range(b-1, t, -1):
                # Go bottom to top (left)
                if (i, l) not in visited:
                    res.append(matrix[i][l])
                visited.add((i, l))
            l += 1
            r-=1
            t+=1
            b-=1
            print(res, "AFTER ONE LOOP")
        return res
        