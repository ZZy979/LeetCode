// 位操作法
class Solution {
    public int[] findClosedNumbers(int num) {
        return new int[] {getNext(num), getPrev(num)};
    }

    private int getNext(int n) {
        // p为最右边但不是结尾的0的位置，p右边0和1的个数分别为c0和c1
        int temp = n, c0 = 0, c1 = 0;
        while (((temp & 1) == 0) && (temp != 0)) {
            ++c0;
            temp >>= 1;
        }
        while ((temp & 1) == 1) {
            ++c1;
            temp >>= 1;
        }
        // n == 11...1100...00
        if (c0 + c1 == 31 || c0 + c1 == 0)
            return -1;
        
        int p = c0 + c1;
        n |= (1 << p);  // 翻转最右非结尾的0
        n &= ~((1 << p) - 1);  // 将p右方的所有位清零
        n |= (1 << (c1 - 1)) - 1;  // 在右侧插入c1-1个1
        return n;
    }

    private int getPrev(int n) {
        // p为最右边但不是结尾的1的位置，p右边0和1的个数分别为c0和c1
        int temp = n, c0 = 0, c1 = 0;
        while ((temp & 1) == 1) {
            ++c1;
            temp >>= 1;
        }
        // n == 00...0011...11
        if (temp == 0)
            return -1;
        while (((temp & 1) == 0) && (temp != 0)) {
            ++c0;
            temp >>= 1;
        }

        int p = c0 + c1;
        n &= (-1 << (p + 1));  // 将第0~p位清零
        n |= ((1 << (c1 + 1)) - 1) << (c0 - 1);  // 在紧邻p的右方插入c1+1个1
        return n;
    }

}
