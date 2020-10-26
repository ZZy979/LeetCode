class Solution {
    public int[] drawLine(int length, int w, int x1, int x2, int y) {  
        int[] screen = new int[length];
        int low = (y * w + x1) / 32;
        int high = (y * w + x2) / 32;
        for (int i = low; i <= high; i++)
            screen[i] = -1;
        screen[low] = screen[low] >>> x1 % 32;
        screen[high] = screen[high] & Integer.MIN_VALUE >> x2 % 32;
        return screen;
    }
}
