class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> wordMap = new HashMap<>();
        for (String s : strs) {
            String sorted = sort(s);
            if (!wordMap.containsKey(sorted)) {
                List<String> list = new ArrayList<>();
                list.add(s);
                wordMap.put(sorted, list);
            }
            else
                wordMap.get(sorted).add(s);
        }
        return new ArrayList<>(wordMap.values());
    }

    private String sort(String s) {
        char[] chars = s.toCharArray();
        Arrays.sort(chars);
        return new String(chars);
    }

}
