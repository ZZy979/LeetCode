class Solution {
    public boolean isUnique(String astr) {
        HashSet<Character> set = new HashSet<>();
        for (char c : astr.toCharArray())
            if (!set.add(c))
                return false;
        return true;
    }
}
