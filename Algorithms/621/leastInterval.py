from collections import Counter

# 官方题解1：模拟，不断地选择不在冷却中并且剩余执行次数最多的那个任务
# 时间复杂度O(|set(tasks)|·|tasks|)，空间复杂度O(|set(tasks)|)
# 1040 ms
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        m = len(freq)
        nextValid = [1] * m
        rest = list(freq.values())

        time = 0
        for i in range(len(tasks)):
            time += 1
            minNextValid = min(nextValid[j] for j in range(m) if rest[j])
            time = max(time, minNextValid)

            # 直接跳过待命状态
            best = max(
                filter(lambda j: rest[j] and nextValid[j] <= time, range(m)),
                key=lambda j: rest[j]
            )
            nextValid[best] = time + n + 1
            rest[best] -= 1
        return time
