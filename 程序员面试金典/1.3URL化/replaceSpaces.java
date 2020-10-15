class Solution {
    public String replaceSpaces(String S, int length) {
        int spaceCount = 0;
        char[] chars = S.toCharArray();
        for (int i = 0; i < length; ++i)
            if (chars[i] == ' ')
                ++spaceCount;
        int index = length + 2 * spaceCount;
        for (int i = length - 1; i >= 0; --i)
            if (chars[i] == ' ') {
                chars[--index] = '0';
                chars[--index] = '2';
                chars[--index] = '%';
            }
            else
                chars[--index] = chars[i];
        // 原字符串长度不一定是length + 2 * spaceCount！！
        return new String(chars, 0, length + 2 * spaceCount);
    }
}
