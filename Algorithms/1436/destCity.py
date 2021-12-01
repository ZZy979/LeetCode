class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        src, dst = set(), set()
        for u, v in paths:
            src.add(u)
            dst.add(v)
        return (dst - src).pop()
