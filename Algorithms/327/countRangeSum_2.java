// 官方题解方法1：归并排序，时间复杂度O(nlog n)，空间复杂度O(n)
// 7 ms
class Solution {
    public int countRangeSum(int[] nums, int lower, int upper) {
        long[] cumsum = calcCumsum(nums);
        return countRangeSumRecursive(cumsum, lower, upper, 0, cumsum.length - 1);
    }

    private long[] calcCumsum(int[] nums) {
        long[] cumsum = new long[nums.length + 1];
        long sum = 0;
        for (int i = 0; i < nums.length; ++i)
            cumsum[i + 1] = (sum += nums[i]);
        return cumsum;
    }

    private int countRangeSumRecursive(long[] cumsum, int lower, int upper, int left, int right) {
        if (left == right)
            return 0;
        else {
            int mid = (left + right) / 2;
            int ret = countRangeSumRecursive(cumsum, lower, upper, left, mid) + countRangeSumRecursive(cumsum, lower, upper, mid + 1, right);

            // 首先统计下标对的数量
            int i = left, l = mid + 1, r = mid + 1;
            while (i <= mid) {
                while (l <= right && cumsum[l] - cumsum[i] < lower)
                    ++l;
                while (r <= right && cumsum[r] - cumsum[i] <= upper)
                    ++r;
                ret += r - l;
                ++i;
            }

            // 随后合并两个排序数组
            int[] sorted = new int[right - left + 1];
            int p1 = left, p2 = mid + 1, p = 0;
            while (p1 <= mid || p2 <= right) {
                if (p1 > mid)
                    sorted[p++] = (int) cumsum[p2++];
                else if (p2 > right)
                    sorted[p++] = (int) cumsum[p1++];
                else {
                    if (cumsum[p1] < cumsum[p2])
                        sorted[p++] = (int) cumsum[p1++];
                    else
                        sorted[p++] = (int) cumsum[p2++];
                }
            }
            for (int j = 0; j < sorted.length; j++)
                cumsum[left + j] = sorted[j];
            return ret;
        }
    }
}
