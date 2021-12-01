class Solution:
    def compressString(self, S: str) -> str:
        if not S:
            return ''
        compressed = []
        last = S[0]
        count = 1
        for i in range(1, len(S)):
            if S[i] == last:
                count += 1
            else:
                compressed.append(last + str(count))
                last = S[i]
                count = 1
        compressed.append(last + str(count))
        compressed_str = ''.join(compressed)
        return S if len(compressed_str) >= len(S) else compressed_str
