class Solution:
    def countAndSay(self, n: int) -> str:
        seq = [1]
        for i in range(1, n):
            seq = self.next_seq(seq)
        return ''.join(str(x) for x in seq)
    
    def next_seq(self, seq):
        temp = []
        n = 1
        x = seq[0]
        for i in range(1, len(seq)):
            if seq[i] == x:
                n += 1
            else:
                temp.append(n)
                temp.append(x)
                n = 1
                x = seq[i]
        temp.append(n)
        temp.append(x)
        return temp
