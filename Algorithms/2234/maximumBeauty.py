class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        n = len(flowers)
        flowers = sorted((min(x, target) for x in flowers), reverse=True)
        total = sum(flowers)
        ans = 0

        if target * n - total <= newFlowers:
            ans = full * n

        pre = ptr = 0
        for i in range(n):
            if i != 0:
                pre += flowers[i - 1]
            if flowers[i] == target:
                continue
            rest = newFlowers - (target * i - pre)
            if rest < 0:
                break
            while not (ptr >= i and flowers[ptr] * (n - ptr) - total <= rest):
                total -= flowers[ptr]
                ptr += 1
            rest -= flowers[ptr] * (n - ptr) - total
            ans = max(ans, full * i + partial * min(flowers[ptr] + rest // (n - ptr), target - 1))
        return ans
