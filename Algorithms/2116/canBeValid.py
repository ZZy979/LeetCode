class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False

        locked_left_indices = []
        unlocked_indices = []
        for i in range(n):
            if s[i] == ')' and locked[i] == '1':
                if locked_left_indices:
                    locked_left_indices.pop()
                elif unlocked_indices:
                    unlocked_indices.pop()
                else:
                    return False
            elif s[i] == '(' and locked[i] == '1':
                locked_left_indices.append(i)
            else:
                unlocked_indices.append(i)

        m = len(unlocked_indices)
        j = 0
        for idx in locked_left_indices:
            while j < m and unlocked_indices[j] < idx:
                j += 1
            if j == m:
                return False
            j += 1
        return True
