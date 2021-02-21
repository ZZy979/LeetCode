// 官方题解2：滑动窗口
// 时间复杂度O(n)，空间复杂度O(1)
// 5 ms
class Solution {
    public int minKBitFlips(int[] A, int K) {
        int ans = 0, revCnt = 0;
        for (int i = 0; i < A.length; ++i) {
            if (i >= K && A[i - K] > 1)
                revCnt ^= 1;
            if (A[i] == revCnt) {
                if (i + K > A.length)
                    return -1;
                ++ans;
                revCnt ^= 1;
                A[i] += 2;
            }
        }
        return ans;
    }
}
