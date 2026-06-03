class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix)-1
        t, b = 0, len(matrix)-1

        def subProblem(l,r,t,b):
            if l > r:
                return
            diff = r - l
            for i in range (diff):
                tmp = matrix[t][l + i]
                matrix[t][l + i] = matrix[b - i][l]
                matrix[b - i][l] = matrix[b][r - i]
                matrix[b][r-i] = matrix[t+i][r]
                matrix[t+i][r] = tmp
            subProblem(l+1,r-1,t+1,b-1)
        return subProblem(l,r,t,b)