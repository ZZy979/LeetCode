// 暴力法
// 时间复杂度O(nk)，空间复杂度O(n)
// 2507 ms
class Solution {
    public int minKBitFlips(int[] A, int K) {
        int[] count = new int[A.length];
        int res = 0;
        for (int i = 0; i < A.length; i++)
            if ((A[i] + count[i]) % 2 == 0) {
                res++;
                for (int j = i; j < i + K; j++) {
                    if (j >= A.length)
                        return -1;
                    count[j]++;
                }
            }
        return res;
    }
}
