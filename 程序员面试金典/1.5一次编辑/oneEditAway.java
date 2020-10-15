class Solution {
    public boolean oneEditAway(String first, String second) {
        if (first.length() < second.length()) {
            String temp = first;
            first = second;
            second = temp;
        }
        if (first.length() - second.length() >= 2)
            return false;
        int i = 0, j = 0;
        boolean foundDiff = false;
        while (i < first.length() && j < second.length()) {
            if (first.charAt(i) != second.charAt(j)) {
                if (foundDiff)
                    return false;
                foundDiff = true;
                if (first.length() == second.length())
                    ++j;
            }
            else
                ++j;
            ++i;
        }
        return true;
    }
}
