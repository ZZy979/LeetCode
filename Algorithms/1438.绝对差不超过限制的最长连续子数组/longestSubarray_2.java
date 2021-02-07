class Solution {
    public int longestSubarray(int[] nums, int limit) {
        Deque<Integer> maxd = new ArrayDeque<>(), mind = new ArrayDeque<>();
        int left = 0, ans = 0;
        for (int right = 0; right < nums.length; ++right) {
            while (!maxd.isEmpty() && nums[right] > maxd.peekLast())
                maxd.pollLast();
            while (!mind.isEmpty() && nums[right] < mind.peekLast())
                mind.pollLast();
            maxd.addLast(nums[right]);
            mind.addLast(nums[right]);
            while (maxd.peek() - mind.peek() > limit) {
                if (maxd.peek() == nums[left])
                    maxd.poll();
                if (mind.peek() == nums[left])
                    mind.poll();
                ++left;
            }
            ans = Math.max(ans, right - left + 1);
        }
        return ans;
    }
}
