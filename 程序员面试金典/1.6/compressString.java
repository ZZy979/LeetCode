class Solution {
    public String compressString(String S) {
        if (S == null || S.length() <= 2)
            return S;
        StringBuilder compressed = new StringBuilder();
        char last = S.charAt(0);
        int count = 0;
        for (char c : S.toCharArray())
            if (c != last) {
                compressed.append(last).append(count);
                last = c;
                count = 1;
            }
            else
                ++count;
        compressed.append(last).append(count);
        return compressed.length() < S.length() ? compressed.toString() : S;
    }
}
