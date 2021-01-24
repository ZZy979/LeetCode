class Solution {
    public List<Integer> addToArrayForm(int[] A, int K) {
        List<Integer> res = new ArrayList<Integer>();
        int n = A.length;
        for (int i = n - 1; i >= 0 || K > 0; --i, K /= 10) {
            if (i >= 0)
                K += A[i];
            res.add(K % 10);
        }
        Collections.reverse(res);
        return res;
    }
}
