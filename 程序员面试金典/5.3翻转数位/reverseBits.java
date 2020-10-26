class Solution {
    public int reverseBits(int num) {
        if (num == -1)
            return 32;
        int currentLength = 0, prevLength = 0, maxLength = 1;
        while (num != 0) {
            if ((num & 1) == 1)
                ++currentLength;
            else {
                prevLength = (num & 2) == 0 ? 0 : currentLength;
                currentLength = 0;
            }
            maxLength = Math.max(maxLength, prevLength + currentLength + 1);
            num >>>= 1;
        }
        return maxLength;
    }
}
