class Solution {
    private List<List<String>> res = new ArrayList<>();

    public List<List<String>> solveNQueens(int n) {
        char[][] grid = new char[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                grid[i][j] = '.';
            }
        }
        boolean[] col = new boolean[n];
        boolean[] dg = new boolean[n + n];
        boolean[] udg = new boolean[n + n];
        dfs(0, n, grid, col, dg, udg);

        return res;
    }

    private void dfs(int h, int n, char[][] grid, boolean[] col, boolean[] dg, boolean[] udg) {
        if (h == n) {
            List<String> list = new ArrayList<>();
            for (int i = 0; i < grid.length; i++) {
                list.add(new String(grid[i]));
            }
            res.add(list);
            return;
        }
        for (int j = 0; j < n; j++) {
            if (!col[j] && !dg[n - h + j] && !udg[h + j]) {
                grid[h][j] = 'Q';
                col[j] = dg[n - h + j] = udg[h + j] = true;
                dfs(h + 1, n, grid, col, dg, udg);
                grid[h][j] = '.';
                col[j] = dg[n - h + j] = udg[h + j] = false;
            }
        }
    }
}
