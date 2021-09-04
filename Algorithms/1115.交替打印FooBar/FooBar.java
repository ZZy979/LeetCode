class FooBar {
    private int n;
    private Semaphore fooSem = new Semaphore(0);
    private Semaphore barSem = new Semaphore(1);

    public FooBar(int n) {
        this.n = n;
    }

    public void foo(Runnable printFoo) throws InterruptedException {
        for (int i = 0; i < n; i++) {
            barSem.acquire();
            // printFoo.run() outputs "foo". Do not change or remove this line.
            printFoo.run();
            fooSem.release();
        }
    }

    public void bar(Runnable printBar) throws InterruptedException {
        for (int i = 0; i < n; i++) {
            fooSem.acquire();
            // printBar.run() outputs "bar". Do not change or remove this line.
            printBar.run();
            barSem.release();
        }
    }
}
