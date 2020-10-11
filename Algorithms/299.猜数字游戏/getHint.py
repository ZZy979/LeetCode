class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        n = len(secret)
        bulls = cows = 0
        judged_a = [False] * n
        judged_b = [False] * n
        for i in range(n):
            if guess[i] == secret[i]:
                bulls += 1
                judged_a[i] = True
        for i in range(n):
            if not judged_a[i]:
                for j in range(n):
                    if not judged_a[j] and not judged_b[j] and guess[i] == secret[j]:
                        cows += 1
                        judged_b[j] = True
                        break
        return '{}A{}B'.format(bulls, cows)
