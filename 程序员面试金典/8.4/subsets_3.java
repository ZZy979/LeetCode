// 方法3：二进制数
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> subsets = new ArrayList<>();
        for (int x = 0; x < Math.pow(2, nums.length); ++x)
            subsets.add(intToSubset(nums, x));
        return subsets;
    }

    private List<Integer> intToSubset(int[] nums, int x) {
        List<Integer> subset = new ArrayList<>();
        for (int i = 0; x != 0; x >>= 1, ++i)
            if ((x & 1) == 1)
                subset.add(nums[i]);
        return subset;
    }

}
