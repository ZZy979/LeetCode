class Solution:
    def findString(self, words: List[str], s: str) -> int:
        left, right = 0, len(words) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_left = mid_right = mid
            while mid_left >= left and not words[mid_left]:
                mid_left -= 1
            while mid_right <= right and not words[mid_right]:
                mid_right += 1
            # [left ... mid_left 空串 mid 空串 mid_right ... right] 
            # mid_left<left => 左半边全是空串，mid_right>right => 右半边全是空串
            if mid_left < left and mid_right > right:
                return -1
            if mid_left >= left:
                if s < words[mid_left]:
                    right = mid_left - 1
                    continue
                elif s == words[mid_left]:
                    return mid_left
                elif mid_right > right:
                    return -1
            if mid_right <= right:
                if s == words[mid_right]:
                    return mid_right
                else:
                    left = mid_right + 1
        return -1
