class Solution {
    private List<String> res = new ArrayList<>();
    private int index = 0;

    public String[] permutation(String S) {
        Map<Character, Integer> count = calcCharCount(S);
        getPerms(count, "", S.length());
        return res.toArray(new String[0]);
    }

    private Map<Character, Integer> calcCharCount(String s) {
        Map<Character, Integer> count = new HashMap<>();
        for (char c : s.toCharArray())
            count.put(c, count.getOrDefault(c, 0) + 1);
        return count;
    }

    private void getPerms(Map<Character, Integer> count, String prefix, int remaining) {
        if (remaining == 0) {
            res.add(prefix);
            return;
        }
        for (char c : count.keySet())
            if (count.get(c) > 0) {
                count.put(c, count.get(c) - 1);
                getPerms(count, prefix + c, remaining - 1);
                count.put(c, count.get(c) + 1);
            }
    }

}
