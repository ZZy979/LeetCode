class Solution {
    public int maximum(int a, int b) {
        long x = a, y = b;
        return (int) ((x + y + Math.abs(x - y)) / 2);
    }
}
