class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        return ' '.join(to_goat_latin(w, i + 1) for i, w in enumerate(sentence.split()))


def to_goat_latin(word, index):
    return (word if word[0] in 'aeiouAEIOU' else word[1:] + word[0]) + 'ma' + 'a' * index
