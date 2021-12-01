class Solution {
    public int[] drawLine(int length, int w, int x1, int x2, int y) {
        int n = w / 32;
        int h = length / n;
        int[] screen = new int[length];
        for (int i = x1; i <= x2; ++i)
            screen[y * n + i / 32] |= (1 << (31 - i % 32));
        return screen;
    }
}
