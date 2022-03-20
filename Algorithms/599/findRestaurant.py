class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d1 = {r: i for i, r in enumerate(list1)}
        min_idx_sum, ans = 0x7fffffff, []
        for i, r in enumerate(list2):
            if r in d1:
                if (s := i + d1[r]) < min_idx_sum:
                    min_idx_sum, ans = s, [r]
                elif s == min_idx_sum:
                    ans.append(r)
        return ans
