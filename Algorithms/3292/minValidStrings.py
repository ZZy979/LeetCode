# 官方题解：KMP+动态规划
# 时间复杂度O(k(m+n))，空间复杂度O(m+n)，其中k是words的长度，m是单词的长度，n是target的长度
class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        n = len(target)
        back = [0] * n
        for word in words:
            pi = prefix_function(word, target)
            m = len(word)
            for i in range(n):
                back[i] = max(back[i], pi[m + 1 + i])
        dp = [0] + [10**9] * n
        for i in range(n):
            dp[i + 1] = dp[i + 1 - back[i]] + 1
            if dp[i + 1] > n:
                return -1
        return dp[n]

def prefix_function(word, target):
    s = word + '#' + target
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi
