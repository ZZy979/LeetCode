class Solution {
    public String toHex(int num) {
        if (num == 0) {
            return "0";
        }
        char[] hex = "0123456789abcdef".toCharArray();
        StringBuilder sb = new StringBuilder();
        while (num != 0 && sb.length() < 8) {
            sb.append(hex[num & 0xf]);
            num >>= 4;
        }
        return sb.reverse().toString();
    }
}
