// 方法2：由S的所有长度为n-1的子序列的排列组合构造S的排列组合（在开头固定每一个字符）
// 70 ms
class Solution {
    public String[] permutation(String S) {
        return getPerms(S).toArray(new String[0]);
    }

    private List<String> getPerms(String s) {
        List<String> permutations = new ArrayList<>();
        if (s.isEmpty()) {
            permutations.add("");
            return permutations;
        }
        for (int i = 0; i < s.length(); ++i)
            for (String perm : getPerms(s.substring(0, i) + s.substring(i + 1)))
                permutations.add(s.charAt(i) + perm);
        return permutations;
    }

}
