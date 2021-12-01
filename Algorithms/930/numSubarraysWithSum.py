class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        n = len(A)
        suma = sum(A)
        if suma < S:
            return 0
        elif S == 0:
            if suma == len(A):
                return 0
            ans = 0
            left = A.index(0)
            while left < n:
                right = left + 1
                while right < n and A[right] == 0:
                    right += 1
                ans += (right - left) * (right - left + 1) // 2
                left = right + 1
                while left < n and A[left] == 1:
                    left += 1
            return ans
        else:
            left = right = A.index(1)
            while S > 0:
                S -= A[right]
                right += 1
            right -= 1
            prev_left = -1
            ans = 0
            while right < n:
                next_right = right + 1
                while next_right < n and A[next_right] == 0:
                    next_right += 1
                ans += (left - prev_left) * (next_right - right)
                prev_left = left
                left += 1
                while left < n and A[left] == 0:
                    left += 1
                right = next_right
            return ans
