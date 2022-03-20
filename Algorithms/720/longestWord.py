class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = {}
        ans = ''
        words.sort(key=len)

        for word in words:
            node = trie
            for i, c in enumerate(word):
                if c not in node:
                    if i < len(word) - 1:
                        break
                    node[c] = {}
                node = node[c]
            else:
                node['#'] = None
                if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                    ans = word
        return ans
