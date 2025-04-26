class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        x = smallest = largest = 0
        for d in differences:
            x += d
            smallest = min(smallest, x)
            largest = max(largest, x)
        return max(upper - lower + 1 - (largest - smallest), 0)
