class Solution {
    public void setZeroes(int[][] matrix) {
        boolean zeroFirstRow = false, zeroFirstCol = false;
        for (int c = 0; c < matrix[0].length; ++c)
            if (matrix[0][c] == 0) {
                zeroFirstRow = true;
                break;
            }
        for (int r = 0; r < matrix.length; ++r)
            if (matrix[r][0] == 0) {
                zeroFirstCol = true;
                break;
            }
        for (int r = 0; r < matrix.length; ++r)
            for (int c = 0; c < matrix[r].length; ++c)
                if (matrix[r][c] == 0)
                    matrix[r][0] = matrix[0][c] = 0;
        for (int r = 1; r < matrix.length; ++r)
            if (matrix[r][0] == 0)
                zeroRow(matrix, r);
        for (int c = 1; c < matrix[0].length; ++c)
            if (matrix[0][c] == 0)
                zeroCol(matrix, c);
        if (zeroFirstRow)
            zeroRow(matrix, 0);
        if (zeroFirstCol)
            zeroCol(matrix, 0);
    }

    private void zeroRow(int[][] matrix, int row) {
        for (int c = 0; c < matrix[row].length; ++c)
            matrix[row][c] = 0;
    }

    private void zeroCol(int[][] matrix, int col) {
        for (int r = 0; r < matrix.length; ++r)
            matrix[r][col] = 0;
    }

}
