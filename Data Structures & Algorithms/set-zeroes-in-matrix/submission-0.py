class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowsToZero = set()
        columnsToZero = set()

        def setWholeRowZero(row, matrix):
            for j in range(len(matrix[0])):
                matrix[row][j] = 0
            
        def setWholeColumnZero(column, matrix):
            for i in range(len(matrix)):
                    matrix[i][column] = 0

        for i in range(len(matrix)):
            for j in range (len(matrix[0])):
                if matrix[i][j] == 0:
                    rowsToZero.add(i)
                    columnsToZero.add(j)
        for r in rowsToZero:
            setWholeRowZero(r, matrix)
        for c in columnsToZero:
            setWholeColumnZero(c, matrix)
        
        
        
     #  [1,2,3]
     #  [4,0,5]
     #  [6,7,8]
    
   

        
        