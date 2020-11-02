// 方法1：由S[1:n]的排列组合构造S的排列组合（S[0]插空）
// 20 ms
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
        String first = s.substring(0, 1);
        for (String perm : getPerms(s.substring(1)))
            for (int i = 0; i <= perm.length(); ++i)
                permutations.add(perm.substring(0, i) + first + perm.substring(i));
        return permutations;
    }

}
