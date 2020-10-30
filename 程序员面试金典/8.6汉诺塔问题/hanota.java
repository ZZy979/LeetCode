class Solution {
    public void hanota(List<Integer> A, List<Integer> B, List<Integer> C) {
        hanoi(A, B, C, A.size());
    }

    private void hanoi(List<Integer> A, List<Integer> B, List<Integer> C, int n) {
        if (n == 1)
            C.add(A.remove(A.size() - 1));
        else {
            hanoi(A, C, B, n - 1);
            C.add(A.remove(A.size() - 1));
            hanoi(B, A, C, n - 1);
        }
    }

}
