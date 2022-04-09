class Solution:
    def uniqueMorseRepresentations(self,  words: List[str]) -> int:
        morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        return len(set(''.join(morse_code[ord(c) - ord('a')] for c in word) for word in words))
