// 官方题解方法2：线段树，时间复杂度O(nlog n)，空间复杂度O(n)
// 41 ms
class SegNode {
    int lo, hi, add = 0;
    SegNode lchild, rchild;

    public SegNode(int lo, int hi) {
        this.lo = lo;
        this.hi = hi;
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
        for (long x : allNumbers)
            values.put(x, idx++);

        SegNode root = build(0, values.size() - 1);
        int ret = 0;
        for (long x : cumsum) {
            int left = values.get(x - upper), right = values.get(x - lower);
            ret += count(root, left, right);
            insert(root, values.get(x));
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

    private SegNode build(int left, int right) {
        SegNode node = new SegNode(left, right);
        if (left == right)
            return node;
        int mid = (left + right) / 2;
        node.lchild = build(left, mid);
        node.rchild = build(mid + 1, right);
        return node;
    }

    private int count(SegNode root, int left, int right) {
        if (left > root.hi || right < root.lo)
            return 0;
        if (left <= root.lo && root.hi <= right)
            return root.add;
        return count(root.lchild, left, right) + count(root.rchild, left, right);
    }

    private void insert(SegNode root, int val) {
        root.add++;
        if (root.lo == root.hi)
            return;
        int mid = (root.lo + root.hi) / 2;
        if (val <= mid)
            insert(root.lchild, val);
        else
            insert(root.rchild, val);
    }

}
