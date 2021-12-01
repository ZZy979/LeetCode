class Solution:
    def findString(self, words: List[str], s: str) -> int:
        left, right = 0, len(words) - 1
        while left <= right:
            origin_mid = mid = (left + right) // 2
            while mid <= right and words[mid] == '':
                mid += 1
            if mid > right:
                right = origin_mid - 1
                continue
            if words[mid] < s:
                left = mid + 1
            elif words[mid] > s:
                right = mid - 1
            else:
                return mid
        return -1
