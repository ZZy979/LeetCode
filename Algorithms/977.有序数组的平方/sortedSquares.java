// 双指针法
// 关键：绝对值最大的一定在两端
class Solution {
    public int[] sortedSquares(int[] A) {
        int[] ans = new int[A.length];
        int left = 0, right = A.length - 1;
        for (int i = ans.length - 1; i >= 0; --i)
            if (Math.abs(A[left]) > Math.abs(A[right])) {
                ans[i] = A[left] * A[left];
                ++left;
            }
            else {
                ans[i] = A[right] * A[right];
                --right;
            }
        return ans;
    }
}
