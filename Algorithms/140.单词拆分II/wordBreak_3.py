class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if len(set(s)) > len(set("".join(wordDict))):
            return []
        wordDict = set(wordDict)
        N = len(s)
        dp = [[] for i in range(N)]
        for i in range(N):
            word = s[:i+1]
            if word in wordDict:
                dp[i].append([i])
        for i in range(N):
            if dp[i]:
                break
        for j in range(i+1, N):
            for k in range(j):
                if dp[k] and s[k+1:j+1] in wordDict:
                    for L in dp[k]:
                        dp[j].append(L[:] + [j])
        L = dp[-1]
        ans = []
        for index in L:
            wordList = [s[:index[0]+1]]
            for i in range(len(index)-1):
                wordList.append(s[index[i]+1:index[i+1]+1])
            ans.append(" ".join(wordList))
        return ans
