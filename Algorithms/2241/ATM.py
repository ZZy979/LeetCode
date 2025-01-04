class ATM:

    def __init__(self):
        self.cnt = [0] * 5
        self.denominations = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.cnt[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        res = [0] * 5
        for i in range(4, -1, -1):
            res[i] = min(amount // self.denominations[i], self.cnt[i])
            amount -= res[i] * self.denominations[i]
        if amount > 0:
            return[-1]
        for i in range(5):
            self.cnt[i] -= res[i]
        return res


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
