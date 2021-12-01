class Solution {
    public String sortString(String s) {
        int[] count = new int[26];
        for (int i = 0; i < s.length(); ++i)
            ++count[s.charAt(i) - 'a'];

        StringBuilder res = new StringBuilder();
        while (res.length() < s.length()) {
            for (int i = 0; i <= 25; ++i)
                if (count[i] > 0) {
                    res.append((char) ('a' + i));
                    --count[i];
                }
            for (int i = 25; i >= 0; --i)
                if (count[i] > 0) {
                    res.append((char) ('a' + i));
                    --count[i];
                }
        }
        return res.toString();
    }
}
