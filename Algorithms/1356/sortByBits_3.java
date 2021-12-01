// 方法3：合二为一
// 3 ms
class Solution {
    public int[] sortByBits(int[] arr) {
        int[] ans = new int[arr.length];
        for (int i = 0; i < arr.length; i++)
            ans[i] = Integer.bitCount(arr[i]) * 10000000 + arr[i];
        Arrays.sort(ans);
        for (int i = 0; i < ans.length; i++)
            ans[i] = ans[i] % 10000000;
        return ans;
    }
}
