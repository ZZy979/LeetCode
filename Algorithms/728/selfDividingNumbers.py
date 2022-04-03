class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [n for n in range(left, right + 1) if all(i != 0 and n % i == 0 for i in map(int, str(n)))]
