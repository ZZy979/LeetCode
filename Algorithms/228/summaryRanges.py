class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        ans = []
        start = None
        for i in range(len(nums)):
            if i == 0:
                start = nums[i]
            elif nums[i] > nums[i - 1] + 1:
                if nums[i - 1] == start:
                    ans.append(str(start))
                else:
                    ans.append('{}->{}'.format(start, nums[i - 1]))
                start = nums[i]
        if nums[-1] == start:
            ans.append(str(start))
        else:
            ans.append('{}->{}'.format(start, nums[-1]))
        return ans
