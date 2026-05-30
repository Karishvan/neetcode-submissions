class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # rowsToZero = set()
        # columnsToZero = set()
        rowZero = False;


        for i in range(len(matrix)):
            for j in range (len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0 # Indicate this column should be zerod
                    if (i == 0):
                        rowZero = True
                    else:
                        matrix[i][0] = 0
        
        for r in range (1, len(matrix)):
            for c in range (1, len(matrix[0])):
                if (matrix[0][c] == 0 or matrix[r][0] == 0):
                    matrix[r][c] = 0
        
        if (matrix[0][0] == 0):
            for r in range(len(matrix)):
                matrix[r][0] = 0
        if (rowZero):
            for c in range(len(matrix[0])):
                matrix[0][c] = 0
        
        
     #  [1,2,3]
     #  [4,0,5]
     #  [6,7,8]

     # [0,1]
     # [1,1]
    
   

        
        