class Solution {
    public String printBin(double num) {
        if (num < 0 || num >= 1)
            return "ERROR";
        StringBuilder sb = new StringBuilder();
        sb.append("0.");
        while (num != 0) {
            if (sb.length() > 32)
                return "ERROR";
            num *= 2;
            if (num >= 1) {
                num -= 1;
                sb.append("1");
            }
            else
                sb.append("0");
        }
        return sb.toString();
    }
}
