class Solution:
    def printBin(self, num: float) -> str:
        ans = ['0', '.']
        for i in range(32):
            if num == 0:
                return ''.join(ans)
            num *= 2
            if num >= 1:
                num -= 1
                ans.append('1')
            else:
                ans.append('0')
        return 'ERROR'
