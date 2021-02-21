// 官方题解1：差分数组
// 时间复杂度O(n)，空间复杂度O(n)
// 6 ms
class Solution {
    public int minKBitFlips(int[] A, int K) {
        int[] diff = new int[A.length + 1];
        int ans = 0, revCnt = 0;
        for (int i = 0; i < A.length; ++i) {
            revCnt += diff[i];
            if ((A[i] + revCnt) % 2 == 0) {
                if (i + K > A.length)
                    return -1;
                ++ans;
                ++revCnt;
                --diff[i + K];
            }
        }
        return ans;
    }
}
