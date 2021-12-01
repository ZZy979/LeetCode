class Solution {
    public String replaceSpaces(String S, int length) {
        char[] chars = S.toCharArray();
        char[] newChars = new char[length * 3];
        int currentIndex = 0;
        for (int i = 0; i < length; ++i)
            if (chars[i] == ' ') {
                newChars[currentIndex++] = '%';
                newChars[currentIndex++] = '2';
                newChars[currentIndex++] = '0';
            }
            else
                newChars[currentIndex++] = chars[i];
        return new String(newChars, 0, currentIndex);
    }
}
