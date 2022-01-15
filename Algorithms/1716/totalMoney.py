class Solution:
    def totalMoney(self, n: int) -> int:
        # 第i周存的钱a[i]=28+7(i-1)=7i+21，第i周周一存的钱=i
        # n天=w周+d天，则总额=a[1]+...+a[w]+(w+1)+...+(w+d)=28w+w(w-1)/2*7+(2w+1+d)d/2
        w, d = divmod(n, 7)
        return 7 * w * (w + 7) // 2 + (2 * w + 1 + d) * d // 2
