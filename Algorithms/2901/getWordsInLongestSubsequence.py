# 动态规划，时间复杂度O(n²L)，空间复杂度O(n)
class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        dp = [0] * n  # dp[i]表示以words[i]结尾的满足条件的最长子序列的长度
        dp[0] = 1
        last = [-1] * n
        for i in range(1, n):
            mx, idx = 0, -1
            for j in range(i):
                if groups[i] != groups[j] and len(words[i]) == len(words[j]) \
                    and hamming_distance(words[i], words[j]) == 1 and dp[j] > mx:
                    mx, idx = dp[j], j
            dp[i], last[i] = mx + 1, idx

        m = 0
        for i in range(1, n):
            if dp[i] > dp[m]:
                m = i

        ans = []
        while m >= 0:
            ans.append(words[m])
            m = last[m]
        ans.reverse()
        return ans

def hamming_distance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))
