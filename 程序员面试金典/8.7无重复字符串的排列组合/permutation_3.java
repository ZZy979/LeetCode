// 方法2-2：由S的所有长度为n-1的子序列的排列组合构造S的排列组合（在开头固定每一个字符）（使用字符数组）
// 3 ms
class Solution {
    private static final int[] FACTORIALS = new int[] {1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880};
    private String[] res;
    private int index = 0;

    public String[] permutation(String S) {
        res = new String[FACTORIALS[S.length()]];
        getPerms(S.toCharArray(), 0);
        return res;
    }

    private void getPerms(char[] a, int k) {
        if (k == a.length) {
            res[index++] = new String(a);
            return;
        }
        getPerms(a, k + 1);
        for (int i = k + 1; i < a.length; ++i) {
            swap(a, i, k);
            getPerms(a, k + 1);
            swap(a, i, k);
        }
    }

    private static void swap(char[] a, int i, int j) {
        a[i] ^= a[j];
        a[j] ^= a[i];
        a[i] ^= a[j];
    }

}
