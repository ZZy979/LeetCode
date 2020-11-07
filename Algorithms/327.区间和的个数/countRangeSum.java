// 暴力法，时间复杂度O(n²)，空间复杂度O(n)
// 207 ms
class Solution {
    public int countRangeSum(int[] nums, int lower, int upper) {
        long[] cumsum = calcCumsum(nums);
        int count = 0;
        for (int i = 0; i < nums.length; ++i)
            for (int j = i; j < nums.length; ++j) {
                long rangeSum = cumsum[j + 1] - cumsum[i];
                if (lower <= rangeSum && rangeSum <= upper)
                    ++count;
            }
        return count;
    }

    private long[] calcCumsum(int[] nums) {
        // 使用long类型，避免-2147483648这种数据导致溢出
        long[] cumsum = new long[nums.length + 1];
        long sum = 0;
        for (int i = 0; i < nums.length; ++i)
            cumsum[i + 1] = (sum += nums[i]);
        return cumsum;
    }

}
