from threading import Semaphore

class Foo:
    def __init__(self):
        self.first_job_done = Semaphore(0)
        self.second_job_done = Semaphore(0)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_job_done.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.first_job_done.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.second_job_done.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.second_job_done.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
