class Solution {
public:
    vector<vector<int>> pathWithObstacles(vector<vector<int>>& obstacleGrid) {
        vector<vector<int>> ans;
        if(!obstacleGrid.size() || !obstacleGrid[0].size())
            return ans;
        int r = obstacleGrid.size(), c = obstacleGrid[0].size();
        if(obstacleGrid[r - 1][c - 1])
            return ans;
        vector<vector<int>> dp(r, vector<int>(c, 0));
        for(int i = 0; i < r; ++i) {
            if(obstacleGrid[i][0] == 1)
                break;
            dp[i][0] = 1;
        }
        for(int j = 0; j < c; ++j) {
            if(obstacleGrid[0][j] == 1)
                break;
            dp[0][j] = 1;
        }
        for(int i = 1; i < r; ++i)
            for(int j = 1; j < c; ++j)
                dp[i][j] = !obstacleGrid[i][j] ? max(dp[i - 1][j], dp[i][j - 1]) : 0;
        if(!dp[r - 1][c - 1])
            return ans;
        int i = r - 1, j = c - 1;
        while(i >= 0 && j >= 0) {
            ans.push_back({i, j});
            if (i - 1 >= 0 && dp[i - 1][j])
                --i;
            else
                --j;
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
