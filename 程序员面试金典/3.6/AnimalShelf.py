from collections import deque

# 将所有动物放在同一个队列中，则队首就是所有动物中最老
# 查找某个种类的最老时，如果队首的种类是需要的种类则直接出队返回
# 否则用一个辅助队列，主队列不断出队加入辅助队列，直到主队列的队首是需要的种类，或者为空（表示没有需要种类的动物）
# 这种做法不需要使用动物编号
class AnimalShelf:

    def __init__(self):
        self.main_queue = deque()
        self.sub_queue = deque()

    def enqueue(self, animal: List[int]) -> None:
        self.main_queue.append(animal)

    def dequeueAny(self) -> List[int]:
        return self.main_queue.popleft() if self.main_queue else [-1, -1]

    def dequeueDog(self) -> List[int]:
        return self.dequeue(1)

    def dequeueCat(self) -> List[int]:
        return self.dequeue(0)
    
    def dequeue(self, animal_num):
        if not self.main_queue:
            return [-1, -1]
        elif self.main_queue[0][1] == animal_num:
            return self.main_queue.popleft()
        else:
            while self.main_queue and self.main_queue[0][1] != animal_num:
                self.sub_queue.append(self.main_queue.popleft())
            animal = self.main_queue.popleft() if self.main_queue else [-1, -1]
            while self.main_queue:
                self.sub_queue.append(self.main_queue.popleft())
            self.main_queue, self.sub_queue = self.sub_queue, self.main_queue
            return animal


# Your AnimalShelf object will be instantiated and called as such:
# obj = AnimalShelf()
# obj.enqueue(animal)
# param_2 = obj.dequeueAny()
# param_3 = obj.dequeueDog()
# param_4 = obj.dequeueCat()
