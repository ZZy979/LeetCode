class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        # a[i] / 2 + 7 < a[j] <= a[i], a[i] >= 15
        n = len(ages)
        ages.sort()
        left = right = ans = 0
        ans = 0
        for a in ages:
            if a < 15:
                continue
            while ages[left] <= 0.5 * a + 7:
                left += 1
            while right < n - 1 and ages[right + 1] <= a:
                right += 1
            ans += right - left
        return ans
