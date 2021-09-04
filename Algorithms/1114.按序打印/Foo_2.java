class Foo {
    private AtomicBoolean firstJobDone = new AtomicBoolean(false);
    private AtomicBoolean secondJobDone = new AtomicBoolean(false);

    public void first(Runnable printFirst) throws InterruptedException {
        // printFirst.run() outputs "first". Do not change or remove this line.
        printFirst.run();
        firstJobDone.set(true);
    }

    public void second(Runnable printSecond) throws InterruptedException {
        while (!firstJobDone.get()) {
        }
        // printSecond.run() outputs "second". Do not change or remove this line.
        printSecond.run();
        secondJobDone.set(true);
    }

    public void third(Runnable printThird) throws InterruptedException {
        while (!secondJobDone.get()) {
        }
        // printThird.run() outputs "third". Do not change or remove this line.
        printThird.run();
    }
}
