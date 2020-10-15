class Solution {
    public boolean CheckPermutation(String s1, String s2) {
        // 先确认字符范围，是ASCII字符串还是Unicode字符串
        if (s1.length() != s2.length())
            return false;
        int[] letters = new int[128];
        for (char c : s1.toCharArray())
            ++letters[c];
        for (char c : s2.toCharArray()) {
            --letters[c];
            if (letters[c] < 0)
                return false;
        }
        return true;
    }
}
