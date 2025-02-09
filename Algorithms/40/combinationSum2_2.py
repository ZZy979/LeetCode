class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse=True)
        return list(backtrack(candidates, 0, target))

def backtrack(candidates, start, target):
    if target == 0:
        yield []
        return
    
    for i in range(start, len(candidates)):
        if candidates[i] <= target:
            break
    else:
        return
    
    for j in range(i, len(candidates)):
        if j == i or candidates[j] < candidates[j - 1]:
            for comb in backtrack(candidates, j + 1, target - candidates[j]):
                yield comb + [candidates[j]]
