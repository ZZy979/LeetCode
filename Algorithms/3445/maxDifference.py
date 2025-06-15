# 官方题解：枚举两个字符+双指针，时间复杂度O(nC²)，空间复杂度O(1)，其中C=5
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        ans = float('-inf')
        for a in '01234':
            for b in '01234':
                if a == b:
                    continue
                
                best = [float('inf')] * 4
                cnt_a = cnt_b = 0
                prev_a = prev_b = 0
                left = -1
                for right in range(n):
                    cnt_a += s[right] == a
                    cnt_b += s[right] == b
                    while right - left >= k and cnt_b - prev_b >= 2:
                        left_status = get_status(prev_a, prev_b)
                        best[left_status] = min(best[left_status], prev_a - prev_b)
                        left += 1
                        prev_a += s[left] == a
                        prev_b += s[left] == b
                    
                    right_status = get_status(cnt_a, cnt_b)
                    if best[right_status ^ 0b10] != float('inf'):
                        ans = max(ans, cnt_a - cnt_b - best[right_status ^ 0b10])
        return ans

def get_status(a, b):
    return ((a & 1) << 1) | (b & 1)
