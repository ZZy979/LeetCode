class Solution:

    def __init__(self):
        self.ans = []
    
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.search(n, k, 1, [])
        return self.ans
    
    def search(self, target, k, start, comb):
        if len(comb) == k:
            if target == 0:
                self.ans.append(comb.copy())
            return
        elif start > 9 or target < start:
            return
        else:
            for i in range(start, 10):
                comb.append(i)
                self.search(target - i, k, i + 1, comb)
                comb.pop()
