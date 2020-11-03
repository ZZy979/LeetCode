class Solution {
    private List<List<String>> solutions = new ArrayList<>();
    private int[] queens;
    private Set<Integer> columns = new HashSet<Integer>();
    private Set<Integer> diagonals1 = new HashSet<Integer>();
    private Set<Integer> diagonals2 = new HashSet<Integer>();

    public List<List<String>> solveNQueens(int n) {
        queens = new int[n];
        Arrays.fill(queens, -1);
        backtrack(0);
        return solutions;
    }

    private void backtrack(int row) {
        if (row == queens.length)
            solutions.add(generateBoard(queens));
        else
            for (int i = 0; i < queens.length; i++) {
                if (!checkValid(row, i))
                    continue;
                queens[row] = i;
                columns.add(i);
                diagonals1.add(row - i);
                diagonals2.add(row + i);
                backtrack(row + 1);
                queens[row] = -1;
                columns.remove(i);
                diagonals1.remove(row - i);
                diagonals2.remove(row + i);
            }
    }

    private List<String> generateBoard(int[] queens) {
        List<String> board = new ArrayList<String>();
        for (int i = 0; i < queens.length; i++) {
            char[] row = new char[queens.length];
            Arrays.fill(row, '.');
            row[queens[i]] = 'Q';
            board.add(new String(row));
        }
        return board;
    }

    private boolean checkValid(int row, int i) {
        return !columns.contains(i) && !diagonals1.contains(row - i) && !diagonals2.contains(row + i);
    }

}
