class Foo {
    private Semaphore firstJobDone = new Semaphore(0);
    private Semaphore secondJobDone = new Semaphore(0);

    public void first(Runnable printFirst) throws InterruptedException {
        // printFirst.run() outputs "first". Do not change or remove this line.
        printFirst.run();
        firstJobDone.release();
    }

    public void second(Runnable printSecond) throws InterruptedException {
        firstJobDone.acquire();
        // printSecond.run() outputs "second". Do not change or remove this line.
        printSecond.run();
        secondJobDone.release();
    }

    public void third(Runnable printThird) throws InterruptedException {
        secondJobDone.acquire();
        // printThird.run() outputs "third". Do not change or remove this line.
        printThird.run();
    }
}
