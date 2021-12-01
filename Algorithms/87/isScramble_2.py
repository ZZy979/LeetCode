# 官方题解：动态规划，时间复杂度O(n^4)，空间复杂度O(n³)
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @cache
        def dfs(i1: int, i2: int, length: int) -> bool:
            """
            第一个字符串从 i1 开始，第二个字符串从 i2 开始，子串的长度为 length，是否和谐
            """

            # 判断两个子串是否相等
            if s1[i1:i1+length] == s2[i2:i2+length]:
                return True
            
            # 判断是否存在字符 c 在两个子串中出现的次数不同
            if Counter(s1[i1:i1+length]) != Counter(s2[i2:i2+length]):
                return False
            
            # 枚举分割位置
            for i in range(1, length):
                # 不交换的情况
                if dfs(i1, i2, i) and dfs(i1 + i, i2 + i, length - i):
                    return True
                # 交换的情况
                if dfs(i1, i2 + length - i, i) and dfs(i1 + i, i2, length - i):
                    return True
        
            return False

        ans = dfs(0, 0, len(s1))
        dfs.cache_clear()
        return ans
