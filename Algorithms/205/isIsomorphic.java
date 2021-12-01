class Solution {
    public boolean isIsomorphic(String s, String t) {
        return isIsomorphicHelper(s, t) && isIsomorphicHelper(t, s);
    }

    private boolean isIsomorphicHelper(String s, String t) {
        int[] map = new int[128];
        char[] cs = s.toCharArray(), ct = t.toCharArray();
        for (int i = 0; i < s.length(); ++i)
            if (map[cs[i]] == 0)
                map[cs[i]] = ct[i];
            else if (map[cs[i]] != ct[i])
                return false;
        return true;
    }

}
