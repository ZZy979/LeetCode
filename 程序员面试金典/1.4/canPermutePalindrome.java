class Solution {
    public boolean canPermutePalindrome(String s) {
        boolean[] oddCount = new boolean[128];
        for (char c : s.toCharArray())
            oddCount[c] = !oddCount[c];
        boolean foundOdd = false;
        for (boolean odd : oddCount)
            if (odd) {
                if (foundOdd)
                    return false;
                foundOdd = true;
            }
        return true;
    }
}
