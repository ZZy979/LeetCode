class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        ticket = 0
        for x in nums:
            if ticket == 0:
                candidate = x
            ticket += 1 if x == candidate else -1
        return candidate
