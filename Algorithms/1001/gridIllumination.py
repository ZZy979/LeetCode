from collections import Counter

class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        lamps = set(map(tuple, lamps))
        row, col, diag1, diag2 = Counter(), Counter(), Counter(), Counter()
        for r, c in lamps:
            row[r] += 1
            col[c] += 1
            diag1[r + c] += 1
            diag2[r - c] += 1
        
        ans = []
        for r, c in queries:
            ans.append(int(row[r] > 0 or col[c] > 0 or diag1[r + c] > 0 or diag2[r - c] > 0))
            for nr in range(r - 1, r + 2):
                for nc in range(c - 1, c + 2):
                    if 0 <= nr < n and 0 <= nc < n and (nr, nc) in lamps:
                        lamps.remove((nr, nc))
                        row[nr] -= 1
                        col[nc] -= 1
                        diag1[nr + nc] -= 1
                        diag2[nr - nc] -= 1
        return ans
