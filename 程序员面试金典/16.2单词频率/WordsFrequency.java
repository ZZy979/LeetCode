class WordsFrequency {
    private Map<String, Integer> count = new HashMap<>();

    public WordsFrequency(String[] book) {
        for (String word : book)
            count.put(word, count.getOrDefault(word, 0) + 1);
    }
    
    public int get(String word) {
        return count.getOrDefault(word, 0);
    }
}

/**
 * Your WordsFrequency object will be instantiated and called as such:
 * WordsFrequency obj = new WordsFrequency(book);
 * int param_1 = obj.get(word);
 */
