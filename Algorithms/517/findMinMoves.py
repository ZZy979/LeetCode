class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total = sum(machines)
        n = len(machines)
        if total % n != 0:
            return -1
        avg = total // n
        ans = s = 0
        for num in machines:
            num -= avg
            s += num
            ans = max(ans, abs(s), num)
        return ans
