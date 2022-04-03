class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        available = list(range(k))
        busy = []
        requests = [0] * k
        for i, (start, t) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= start:
                _, id = heappop(busy)
                heappush(available, i + (id - i) % k)  # 利用 Python 负数取模变成同余的非负数的性质
            if available:
                id = heappop(available) % k
                requests[id] += 1
                heappush(busy, (start + t, id))
        maxRequest = max(requests)
        return [i for i, req in enumerate(requests) if req == maxRequest]
