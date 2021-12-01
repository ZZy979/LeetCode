// 官方题解2：桶
// 时间复杂度O(n)，空间复杂度O(min{n,k})
class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        int n = nums.length;
        Map<Long, Long> map = new HashMap<Long, Long>();
        long w = (long) t + 1;
        for (int i = 0; i < n; i++) {
            long id = getID(nums[i], w);
            if (map.containsKey(id))
                return true;
            if (map.containsKey(id - 1) && Math.abs(nums[i] - map.get(id - 1)) < w)
                return true;
            if (map.containsKey(id + 1) && Math.abs(nums[i] - map.get(id + 1)) < w)
                return true;
            map.put(id, (long) nums[i]);
            if (i >= k)
                map.remove(getID(nums[i - k], w));
        }
        return false;
    }

    public long getID(long x, long w) {
        return x >= 0 ? x / w : (x + 1) / w - 1;
    }
}
