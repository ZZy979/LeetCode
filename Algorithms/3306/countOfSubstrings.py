from collections import Counter

# 滑动窗口，时间复杂度O(n)，空间复杂度O(1)
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        return count(word, k) - count(word, k + 1)


def count(word, k):
    """每个元音字母至少出现一次，并且至少包含k个辅音字母的子字符串的数量"""
    vowels = set('aeiou')
    n, ans, consonants = len(word), 0, 0
    cnt = Counter()
    right = 0
    for left in range(n):
        while right < n and (consonants < k or any(cnt[v] == 0 for v in vowels)):
            if word[right] in vowels:
                cnt[word[right]] += 1
            else:
                consonants += 1
            right += 1
        if consonants >= k and all(cnt[v] > 0 for v in vowels):
            ans += n - right + 1
        if word[left] in vowels:
            cnt[word[left]] -= 1
        else:
            consonants -= 1
    return ans
