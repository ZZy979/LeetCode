class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {c: i for i, c in enumerate(order)}
        return all(cmp(words[i], words[i + 1], order_map) <= 0 for i in range(len(words) - 1))


def cmp(s, t, order_map):
    for a, b in zip(s, t):
        if a != b:
            return order_map[a] - order_map[b]
    return len(s) - len(t)
