// 方法1：迭代
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        ans.add(new ArrayList<>());
        for (int n : nums) {
            int size = ans.size();
            for (int i = 0; i < size; ++i) {
                List<Integer> temp = (ArrayList<Integer>) ((ArrayList<Integer>) ans.get(i)).clone();
                temp.add(n);
                ans.add(temp);
            }
        }
        return ans;
    }
}
