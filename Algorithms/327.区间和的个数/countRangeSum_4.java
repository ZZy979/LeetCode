// 官方题解方法4：树状数组，时间复杂度O(nlog n)，空间复杂度O(n)
// 34 ms
class BIT {
    int[] tree;
    int n;

    public BIT(int n) {
        this.n = n;
        this.tree = new int[n + 1];
    }

    public static int lowbit(int x) {
        return x & (-x);
    }

    public void update(int x, int d) {
        while (x <= n) {
            tree[x] += d;
            x += lowbit(x);
        }
    }

    public int query(int x) {
        int ans = 0;
        while (x != 0) {
            ans += tree[x];
            x -= lowbit(x);
        }
        return ans;
    }

}

class Solution {
    public int countRangeSum(int[] nums, int lower, int upper) {
        long[] cumsum = calcCumsum(nums);
        Set<Long> allNumbers = new TreeSet<>();
        for (long x : cumsum) {
            allNumbers.add(x);
            allNumbers.add(x - lower);
            allNumbers.add(x - upper);
        }
        // 利用哈希表进行离散化
        Map<Long, Integer> values = new HashMap<>();
        int idx = 0;
        for (long x: allNumbers)
            values.put(x, idx++);

        int ret = 0;
        BIT bit = new BIT(values.size());
        for (int i = 0; i < cumsum.length; i++) {
            int left = values.get(cumsum[i] - upper), right = values.get(cumsum[i] - lower);
            ret += bit.query(right + 1) - bit.query(left);
            bit.update(values.get(cumsum[i]) + 1, 1);
        }
        return ret;
    }

    private long[] calcCumsum(int[] nums) {
        long[] cumsum = new long[nums.length + 1];
        long sum = 0;
        for (int i = 0; i < nums.length; ++i)
            cumsum[i + 1] = (sum += nums[i]);
        return cumsum;
    }

}
