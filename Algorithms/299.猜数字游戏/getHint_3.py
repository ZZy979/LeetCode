from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = sum(1 for i in range(len(secret)) if guess[i] == secret[i])
        cows = sum((Counter(secret) & Counter(guess)).values()) - bulls
        return f'{bulls}A{cows}B'
