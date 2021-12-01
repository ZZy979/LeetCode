class Solution {
    public int maximum(int a, int b) {
        int k = (int) (((long) a - (long) b) >> 63);
        return (~k & a) | (k & b);
    }
}
