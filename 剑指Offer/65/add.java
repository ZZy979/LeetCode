class Solution {
    public int add(int a, int b) {
        int carry = 0, s = 0;
        for (int i = 0; i < 32; ++i) {
            int x = a & 1, y = b & 1;
            s |= (carry ^ x ^ y) << i;
            carry = carry & (x ^ y) ^ (x & y);
            a >>= 1;
            b >>= 1;
        }
        return s;
    }
}
