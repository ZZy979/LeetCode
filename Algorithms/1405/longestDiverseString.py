class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        rest = [[a, 'a'], [b, 'b'], [c, 'c']]
        ans = []
        while True:
            rest.sort(reverse=True)
            for p in rest:
                if p[0] and ans[-2:] != [p[1], p[1]]:
                    ans.append(p[1])
                    p[0] -= 1
                    break
            else:
                break
        return ''.join(ans)
