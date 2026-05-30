class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        final int ROWS = matrix.length;
        final int COLS = matrix[0].length;
        int top = 0, bot = ROWS-1;

        int correctRow = 0;
        while (top <= bot){
            int row = (top + bot)/2;
            if (target > matrix[row][COLS-1]){
                top = row+1;
            } else if (target < matrix[row][0]){
                bot = row-1;
            } else {
                correctRow = row;
                break;
            }
        }

        int l = 0;
        int r = COLS-1;
        while (l <= r ){
            int col = (l + r)/2;
            if (target > matrix[correctRow][col]){
                l = col+1;
            } else if (target < matrix[correctRow][col]){
                r = col-1;
            } else {
                return true;
            }
        }
        return false;



        // int rowBot = 0;
        // int colBot = 0;

        // int rowTop = matrix.length-1;
        // int colTop = matrix[0].length-1;

        // while (rowBot <= rowTop && colBot <= colTop){
        //     int rowMid = (rowBot + rowTop)/2;
        //     int colMid = (colBot + colTop)/2;

        //     if (matrix[rowMid][colMid] > target){
        //         if (rowTop == rowBot){
        //             colTop = colMid-1;
        //         } else {
        //             rowTop = rowMid;
        //         }
                
        //     } else if (matrix[rowMid][colMid] < target){
        //         if (rowTop == rowBot){
        //             colBot = colMid+1;
        //         } else {
        //             rowBot = rowMid;
        //         }
                
        //     } else {
        //         return true;
        //     }
        // }
        // return false;
    }
}
