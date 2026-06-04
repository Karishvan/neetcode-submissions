class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r, t, b = 0, len(matrix[0])-1, 0 , len(matrix)-1
        #visited = set()
        res = []
        print(r)
        while l <= r and t <= b:
            for i in range(l, r+1):
                # Go left to right (top)
                res.append(matrix[t][i])
            print(res)
            print(t+1, b+1)
            for j in range(t+1, b+1):
                # Go top to bottom (right)
                res.append(matrix[j][r])
            print(res)
            print(r-1, l-1)
            if t == b or l == r:
                break;
            for k in range(r-1, l-1, -1):
                # Go right to left (bottom)
                res.append(matrix[b][k])
            print(res, "HI")
            for i in range(b-1, t, -1):
                # Go bottom to top (left)
                res.append(matrix[i][l])
            l += 1
            r-=1
            t+=1
            b-=1
            print(res, "AFTER ONE LOOP")
        return res
        