// 官方题解1：滑动窗口+有序集合
// 时间复杂度O(nlog min{n,k})，空间复杂度O(min{n,k})
class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        int n = nums.length;
        TreeSet<Long> set = new TreeSet<Long>();
        for (int i = 0; i < n; i++) {
            Long ceiling = set.ceiling((long) nums[i] - (long) t);
            if (ceiling != null && ceiling <= (long) nums[i] + (long) t)
                return true;
            set.add((long) nums[i]);
            if (i >= k)
                set.remove((long) nums[i - k]);
        }
        return false;
    }
}
