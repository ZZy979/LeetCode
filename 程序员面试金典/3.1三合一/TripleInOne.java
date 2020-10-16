class TripleInOne {
    private int stackSize;
    private int[] data;
    private int[] size;

    public TripleInOne(int stackSize) {
        this.stackSize = stackSize;
        this.data = new int[3 * stackSize];
        this.size = new int[3];
    }
    
    public void push(int stackNum, int value) {
        if (size[stackNum] < stackSize) {
            data[stackNum * stackSize + size[stackNum]] = value;
            ++size[stackNum];
        }
    }
    
    public int pop(int stackNum) {
        if (size[stackNum] == 0)
            return -1;
        else {
            --size[stackNum];
            return data[stackNum * stackSize + size[stackNum]];
        }
    }
    
    public int peek(int stackNum) {
        return size[stackNum] == 0 ? -1 : data[stackNum * stackSize + size[stackNum] - 1];
    }
    
    public boolean isEmpty(int stackNum) {
        return size[stackNum] == 0;
    }
}

/**
 * Your TripleInOne object will be instantiated and called as such:
 * TripleInOne obj = new TripleInOne(stackSize);
 * obj.push(stackNum,value);
 * int param_2 = obj.pop(stackNum);
 * int param_3 = obj.peek(stackNum);
 * boolean param_4 = obj.isEmpty(stackNum);
 */
