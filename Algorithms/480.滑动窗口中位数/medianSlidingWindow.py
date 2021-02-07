# 官方题解：双优先队列+延迟删除
# 时间复杂度O(nlog n)，空间复杂度O(n)
# 116 ms
class DualHeap:
    def __init__(self, k: int):
        # 大根堆，维护较小的一半元素
        self.small = []
        # 小根堆，维护较大的一半元素
        self.large = []
        # 哈希表，记录「延迟删除」的元素，key 为元素，value 为需要删除的次数
        self.delayed = collections.Counter()

        self.k = k
        # small 和 large 当前包含的元素个数，需要扣除被「延迟删除」的元素
        self.smallSize = 0
        self.largeSize = 0

    # 不断地弹出 heap 的堆顶元素，并且更新哈希表
    def prune(self, heap: List[int]):
        while heap:
            num = heap[0]
            if heap is self.small:
                num = -num
            if num in self.delayed:
                self.delayed[num] -= 1
                if self.delayed[num] == 0:
                    self.delayed.pop(num)
                heapq.heappop(heap)
            else:
                break
    
    # 调整 small 和 large 中的元素个数，使得二者的元素个数满足要求
    def makeBalance(self):
        if self.smallSize > self.largeSize + 1:
            # small 比 large 元素多 2 个
            heapq.heappush(self.large, -heapq.heappop(self.small))
            self.smallSize -= 1
            self.largeSize += 1
            # small 堆顶元素被移除，需要进行 prune
            self.prune(self.small)
        elif self.smallSize < self.largeSize:
            # large 比 small 元素多 1 个
            heapq.heappush(self.small, -heapq.heappop(self.large))
            self.smallSize += 1
            self.largeSize -= 1
            # large 堆顶元素被移除，需要进行 prune
            self.prune(self.large)

    def insert(self, num: int):
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
            self.smallSize += 1
        else:
            heapq.heappush(self.large, num)
            self.largeSize += 1
        self.makeBalance()

    def erase(self, num: int):
        self.delayed[num] += 1
        if num <= -self.small[0]:
            self.smallSize -= 1
            if num == -self.small[0]:
                self.prune(self.small)
        else:
            self.largeSize -= 1
            if num == self.large[0]:
                self.prune(self.large)
        self.makeBalance()

    def getMedian(self) -> float:
        return float(-self.small[0]) if self.k % 2 == 1 else (-self.small[0] + self.large[0]) / 2


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        dh = DualHeap(k)
        for num in nums[:k]:
            dh.insert(num)
        
        ans = [dh.getMedian()]
        for i in range(k, len(nums)):
            dh.insert(nums[i])
            dh.erase(nums[i - k])
            ans.append(dh.getMedian())
        return ans
