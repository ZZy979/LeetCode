# 用数学归纳法证明N为奇数时必输，N为偶数时必赢
# ①N=1时必输，N=2时必赢
# ②N>=3时，若N为奇数，则x一定是奇数，N-x一定是偶数，则Bob必赢，Alice必输；
# 若N为偶数，则可以选择x=1，N-x为奇数，则Bob必输，Alice必赢
# 由①②可得Alice赢等价于N为偶数
class Solution:
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0
