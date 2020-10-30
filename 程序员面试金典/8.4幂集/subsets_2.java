// 方法2：递归
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        return getSubsets(nums, nums.length - 1);
    }

    private List<List<Integer>> getSubsets(int[] nums, int index) {
        List<List<Integer>> subsets;
        if (index == -1) {
            subsets = new ArrayList<>();
            subsets.add(new ArrayList<>());
        }
        else {
            subsets = getSubsets(nums, index - 1);
            int size = subsets.size();
            for (int i = 0; i < size; ++i) {
                List<Integer> temp = (ArrayList<Integer>) ((ArrayList<Integer>) subsets.get(i)).clone();
                temp.add(nums[index]);
                subsets.add(temp);
            }
        }
        return subsets;
    }

}
