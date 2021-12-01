// 方法2：递推预处理（根据数据范围0 <= arr[i] <= 10^4）
// 11 ms
class Solution {
    public int[] sortByBits(int[] arr) {
        List<Integer> list = new ArrayList<>();
		for (int x : arr)
			list.add(x);
		int[] bit = new int[10001];
		for (int i = 1; i <= 10000; ++i)
			bit[i] = bit[i >> 1] + (i & 1);
		list.sort((x, y) -> bit[x] != bit[y] ? bit[x] - bit[y] : x - y);
		for (int i = 0; i < arr.length; ++i)
			arr[i] = list.get(i);
        return arr;
    }
}
