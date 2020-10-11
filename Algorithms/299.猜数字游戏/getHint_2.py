class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret = list(secret)
        guess = list(guess)
        bulls = cows = 0
        i = 0
        while i < len(guess):
            if guess[i] == secret[i]:
                bulls += 1
                guess.pop(i)
                secret.pop(i)
            else:
                i += 1
        i = 0
        while i < len(guess):
            if guess[i] in secret:
                cows += 1
                secret.remove(guess[i])
            i += 1
        return '{}A{}B'.format(bulls, cows)
