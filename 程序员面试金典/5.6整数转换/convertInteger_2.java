class Solution {
    public int convertInteger(int A, int B) {
        int count = 0;
        // c &= (c - 1)会清除c的最低有效位
        for (int c = A ^ B; c != 0; c &= (c - 1))
            ++count;
        return count;
    }
}
