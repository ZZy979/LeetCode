class Solution:
    def lengthLongestPath(self, input: str) -> int:
        names = input.split('\n')
        name_lengths, cur_length, ans = [], 0, 0
        for name in names:
            depth = name.rfind('\t') + 1
            length = len(name) - depth
            if depth > len(name_lengths) - 1:
                name_lengths.append(length)
                cur_length += length
            else:
                cur_length += length - sum(name_lengths[depth:])
                name_lengths[depth:] = [length]
            if '.' in name:
                ans = max(ans, cur_length + depth)
        return ans
