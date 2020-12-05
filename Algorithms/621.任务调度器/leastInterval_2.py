from collections import Counter

# 官方题解2：构造
# 时间复杂度O(|tasks|)，空间复杂度O(|set(tasks)|)
# 68 ms
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        # 最多的执行次数
        maxExec = freq.most_common(1)[0][1]
        # 具有最多执行次数的任务数量
        maxCount = list(freq.values()).count(maxExec)
        return max((maxExec - 1) * (n + 1) + maxCount, len(tasks))
