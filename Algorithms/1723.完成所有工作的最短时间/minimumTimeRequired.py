# 官方题解：二分查找+回溯+剪枝
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        jobs.sort(reverse=True)
        left, right = jobs[0], sum(jobs)
        while left < right:
            mid = (left + right) // 2
            if backtrack(jobs, [0] * k, 0, mid):
                right = mid
            else:
                left = mid + 1
        return left


def backtrack(jobs, workloads, i, limit):
    if i == len(jobs):
        return True
    job = jobs[i]
    for j in range(len(workloads)):
        if workloads[j] + job <= limit:
            workloads[j] += job
            if backtrack(jobs, workloads, i + 1, limit):
                return True
            workloads[j] -= job
        if workloads[j] == 0 or workloads[j] + job == limit:
            break
    return False
