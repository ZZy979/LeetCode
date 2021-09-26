class Solution {
    public int getSum(int a, int b) {
        int c = 0, p = 1, sum = 0;
        for (int i = 0; i < 32; ++i) {
            int x = a & 1, y = b & 1, s = x ^ y ^ c;
            c = x & y | c & (x | y);
            if (s == 1) {
                sum |= p;
            }
            p <<= 1;
            a >>= 1;
            b >>= 1;
        }
        return sum;
    }
}
