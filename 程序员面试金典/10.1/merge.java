class Solution {
    public void merge(int[] A, int m, int[] B, int n) {
        int p = A.length - 1;
        --m;
        --n;
        while (m >= 0 && n >= 0)
            A[p--] = B[n] >= A[m] ? B[n--] : A[m--];
        while (n >= 0)
            A[p--] = B[n--];
    }
}
