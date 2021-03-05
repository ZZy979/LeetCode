class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        for x in nums:
            if x in seen:
                seen.remove(x)
            else:
                seen.add(x)
        return list(seen)
