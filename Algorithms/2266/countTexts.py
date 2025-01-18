class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        n = len(pressedKeys)
        q = 10**9 + 7
        dp = [0] * n  # dp[i]表示pressedKeys[0..i]可能有多少种文字信息
        dp[0] = 1
        for i in range(1, n):
            k = pressedKeys[i]
            dp[i] = dp[i - 1]
            nchars = 4 if k in '79' else 3
            j = i - 1
            while j >= max(0, i - nchars + 1) and k == pressedKeys[j]:
                dp[i] = (dp[i] + (1 if j == 0 else dp[j - 1])) % q
                j -= 1
        return dp[-1]
