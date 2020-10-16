class AnimalShelf {
    private Queue<int[]> catQueue, dogQueue;

    public AnimalShelf() {
        catQueue = new LinkedList();
        dogQueue = new LinkedList();
    }
    
    public void enqueue(int[] animal) {
        if (animal[1] == 0)
            catQueue.offer(animal);
        else
            dogQueue.offer(animal);
    }
    
    public int[] dequeueAny() {
        if (catQueue.isEmpty() && dogQueue.isEmpty())
            return new int[] {-1, -1};
        else if (catQueue.isEmpty())
            return dequeueDog();
        else if (dogQueue.isEmpty())
            return dequeueCat();
        else
            return catQueue.peek()[0] < dogQueue.peek()[0] ? dequeueCat() : dequeueDog();
    }
    
    public int[] dequeueDog() {
        return dogQueue.isEmpty() ? new int[] {-1, -1} : dogQueue.poll();
    }
    
    public int[] dequeueCat() {
        return catQueue.isEmpty() ? new int[] {-1, -1} : catQueue.poll();
    }

}

/**
 * Your AnimalShelf object will be instantiated and called as such:
 * AnimalShelf obj = new AnimalShelf();
 * obj.enqueue(animal);
 * int[] param_2 = obj.dequeueAny();
 * int[] param_3 = obj.dequeueDog();
 * int[] param_4 = obj.dequeueCat();
 */
