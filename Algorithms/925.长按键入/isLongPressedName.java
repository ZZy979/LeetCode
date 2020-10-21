// 官方题解：双指针
class Solution {
    public boolean isLongPressedName(String name, String typed) {
        char[] nameChars = name.toCharArray(), typedChars = typed.toCharArray();
        int i = 0, j = 0;
        while (j < typedChars.length) {
            if (i < nameChars.length && nameChars[i] == typedChars[j]) {
                i++;
                j++;
            }
            else if (j > 0 && typedChars[j] == typedChars[j - 1])
                j++;
            else
                return false;
        }
        return i == nameChars.length;
    }
}
