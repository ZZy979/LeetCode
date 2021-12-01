class Solution:
    def __init__(self):
        self.ans = []
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.search(candidates, target, 0, [])
        return self.ans
    
    def search(self, candidates, target, start, comb):
        if target == 0:
            self.ans.append(comb.copy())
        elif target < candidates[start]:
            return
        else:
            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                self.search(candidates, target - candidates[i], i, comb)
                comb.pop()
