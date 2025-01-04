class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return '-'.join(bin(int(s))[2:] for s in date.split('-'))
