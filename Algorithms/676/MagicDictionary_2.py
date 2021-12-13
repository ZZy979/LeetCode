from collections import defaultdict

class MagicDictionary:

    def __init__(self):
        self.buckets = defaultdict(list)

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.buckets[len(word)].append(word)

    def search(self, searchWord: str) -> bool:
        return any(sum(a != b for a, b in zip(searchWord, w)) == 1 for w in self.buckets[len(searchWord)])


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
