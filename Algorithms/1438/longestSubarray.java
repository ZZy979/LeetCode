class Solution {
    public int longestSubarray(int[] nums, int limit) {
        int left = 0, ans = 0;
        TreeMap<Integer, Integer> m = new TreeMap<>();
        for (int right = 0; right < nums.length; ++right) {
            m.put(nums[right], m.getOrDefault(nums[right], 0) + 1);
            while (m.lastKey() - m.firstKey() > limit) {
                m.put(nums[left], m.get(nums[left]) - 1);
                if (m.get(nums[left]) == 0)
                    m.remove(nums[left]);
                ++left;
            }
            ans = Math.max(ans, right - left + 1);
        }
        return ans;
    }
}
