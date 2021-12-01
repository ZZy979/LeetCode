class Solution {
    public int waysToStep(int n) {
        if (n <= 2)
            return n;
        else if (n == 3)
            return 4;
        int a = 1, b = 2, c = 4;
        for (int i = 4; i <= n; ++i) {
            int temp = ((a + b) % 1000000007 + c) % 1000000007;
            a = b;
            b = c;
            c = temp;
        }
        return c;
    }
}
