// 官方题解：双指针法，时间复杂度O(|S|+|T|)，空间复杂度O(1)
class Solution {
    public boolean backspaceCompare(String S, String T) {
        int i = S.length() - 1, j = T.length() - 1;
        int skipS = 0, skipT = 0;

        while (i >= 0 || j >= 0) {
            while (i >= 0) {
                if (S.charAt(i) == '#') {
                    skipS++;
                    i--;
                }
                else if (skipS > 0) {
                    skipS--;
                    i--;
                }
                else
                    break;
            }
            while (j >= 0) {
                if (T.charAt(j) == '#') {
                    skipT++;
                    j--;
                }
                else if (skipT > 0) {
                    skipT--;
                    j--;
                }
                else
                    break;
            }
            if (i >= 0 && j >= 0) {
                if (S.charAt(i) != T.charAt(j))
                    return false;
            }
            else {
                if (i >= 0 || j >= 0)
                    return false;
            }
            i--;
            j--;
        }
        return true;
    }
}
