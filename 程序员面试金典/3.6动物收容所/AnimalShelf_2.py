from collections import deque

# 为猫和狗各自创建一个队列
class AnimalShelf:

    def __init__(self):
        self.cat_queue = deque()
        self.dog_queue = deque()

    def enqueue(self, animal: List[int]) -> None:
        if animal[1] == 0:
            self.cat_queue.append(animal)
        else:
            self.dog_queue.append(animal)

    def dequeueAny(self) -> List[int]:
        if not self.cat_queue and not self.dog_queue:
            return [-1, -1]
        elif not self.cat_queue:
            return self.dequeueDog()
        elif not self.dog_queue:
            return self.dequeueCat()
        else:
            return self.dequeueCat() if self.cat_queue[0][0] < self.dog_queue[0][0] else self.dequeueDog()

    def dequeueDog(self) -> List[int]:
        return self.dog_queue.popleft() if self.dog_queue else [-1, -1]

    def dequeueCat(self) -> List[int]:
        return self.cat_queue.popleft() if self.cat_queue else [-1, -1]


# Your AnimalShelf object will be instantiated and called as such:
# obj = AnimalShelf()
# obj.enqueue(animal)
# param_2 = obj.dequeueAny()
# param_3 = obj.dequeueDog()
# param_4 = obj.dequeueCat()
