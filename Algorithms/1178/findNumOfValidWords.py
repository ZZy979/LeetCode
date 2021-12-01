# 官方题解
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        frequency = collections.Counter()
        for word in words:
            mask = 0
            for c in word:
                mask |= (1 << (ord(c) - ord('a')))
            if bin(mask).count('1') <= 7:
                frequency[mask] += 1
        
        ans = []
        for puzzle in puzzles:
            total = 0

            # 枚举子集方法一
            # for choose in range(1 << 6):
            #     mask = 0
            #     for i in range(6):
            #         if choose & (1 << i):
            #             mask |= (1 << (ord(puzzle[i + 1]) - ord('a')))
            #     mask |= (1 << (ord(puzzle[0]) - ord('a')))
            #     if mask in frequency:
            #         total += frequency[mask]

            # 枚举子集方法二
            mask = 0
            for i in range(1, 7):
                mask |= (1 << (ord(puzzle[i]) - ord('a')))
            subset = mask
            while subset:
                s = subset | (1 << (ord(puzzle[0]) - ord('a')))
                if s in frequency:
                    total += frequency[s]
                subset = (subset - 1) & mask
            
            # 在枚举子集的过程中，要么会漏掉全集 mask，要么会漏掉空集
            # 这里会漏掉空集，因此需要额外判断空集
            if (1 << (ord(puzzle[0]) - ord('a'))) in frequency:
                total += frequency[1 << (ord(puzzle[0]) - ord('a'))]
            ans.append(total)
        return ans
