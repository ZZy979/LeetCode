class Solution {
    private List<String> res = new ArrayList<>();

    public List<String> generateParenthesis(int n) {
        char[] a = new char[2 * n];
        generate(a, 0, n, n);
        return res;
    }

    private void generate(char[] a, int index, int left, int right) {
        if (left < 0 || right < left)
            return;
        if (left == 0 && right == 0) {
            res.add(new String(a));
            return;
        }
        a[index] = '(';
        generate(a, index + 1, left - 1, right);
        a[index] = ')';
        generate(a, index + 1, left, right - 1);
    }

}
