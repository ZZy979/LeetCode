# 官方题解一：枚举，时间复杂度O(n²)，空间复杂度O(1)
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        n = len(word)
        return word if numFriends == 1 else max(word[i:min(i + n - numFriends + 1, n)] for i in range(n))
