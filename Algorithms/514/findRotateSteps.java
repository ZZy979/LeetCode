// 官方题解：dp[i][j]表示从前往后拼写出key的第i个字符，ring的第j个字符与12:00方向对齐的最少步数（下标均从0开始）
class Solution {
    public int findRotateSteps(String ring, String key) {
        int n = ring.length(), m = key.length();
        List<Integer>[] pos = new List[26];
        for (int i = 0; i < 26; ++i)
            pos[i] = new ArrayList<Integer>();
        for (int i = 0; i < n; ++i)
            pos[ring.charAt(i) - 'a'].add(i);
        int[][] dp = new int[m][n];
        for (int i = 0; i < m; ++i)
            Arrays.fill(dp[i], 0x3f3f3f);
        for (int i : pos[key.charAt(0) - 'a'])
            dp[0][i] = Math.min(i, n - i) + 1;
        for (int i = 1; i < m; ++i)
            for (int j : pos[key.charAt(i) - 'a'])
                for (int k : pos[key.charAt(i - 1) - 'a'])
                    dp[i][j] = Math.min(dp[i][j], dp[i - 1][k] + Math.min(Math.abs(j - k), n - Math.abs(j - k)) + 1);
        return Arrays.stream(dp[m - 1]).min().getAsInt();
    }
}
