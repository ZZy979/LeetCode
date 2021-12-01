// 方法1：暴力法
// 17 ms
class Solution {
    public int[] sortByBits(int[] arr) {
        List<Item> items = new ArrayList<>();
		for (int x : arr)
			items.add(new Item(x, Integer.bitCount(x)));
		items.sort(Comparator.comparing(Item::getBitCount).thenComparing(Item::getNum));
		return items.stream().mapToInt(Item::getNum).toArray();
    }
}

class Item {
	int num;
	int bitCount;

	Item(int num, int bitCount) {
		this.num = num;
		this.bitCount = bitCount;
	}

	public int getNum() {
		return num;
	}

	public int getBitCount() {
		return bitCount;
	}

}
