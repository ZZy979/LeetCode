class Solution:
    def reverseBits(self, num: int) -> int:
        counts = []
        count = 0
        while num:
            if num % 2 == 1:
                count += 1
            else:
                counts.append(count)
                count = 0
            num //= 2
        counts.append(count)
        return max(counts[i] + counts[i + 1] + 1 for i in range(len(counts) - 1)) if len(counts) > 1 else counts[0] + 1
