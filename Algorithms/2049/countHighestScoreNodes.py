class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        tree = build_tree(parents)
        size = [0] * n
        calc_size(tree, size, 0)

        max_score, ans = 0, 0
        for v in range(n):
            if (score := calc_score(tree, size, v)) > max_score:
                max_score, ans = score, 1
            elif score == max_score:
                ans += 1
        return ans


def build_tree(parents):
    tree = [[] for _ in range(len(parents))]
    for i in range(1, len(parents)):
        tree[parents[i]].append(i)
    return tree


def calc_size(tree, size, v):
    if size[v] != 0:
        return size[v]
    size[v] = 1 + sum(calc_size(tree, size, u) for u in tree[v])
    return size[v]


def calc_score(tree, size, v):
    if v == 0:
        return math.prod(size[u] for u in tree[v])
    else:
        return (size[0] - size[v]) * math.prod(size[u] for u in tree[v])
