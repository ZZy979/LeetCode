class StackOfPlates {
    private List<Stack<Integer>> stacks;
    private int cap;

    public StackOfPlates(int cap) {
        this.stacks = new ArrayList<>();
        this.cap = cap;
    }
    
    public void push(int val) {
        if (cap == 0)
            return;
        if (stacks.isEmpty() || stacks.get(stacks.size() - 1).size() == cap) {
            Stack<Integer> stack = new Stack<>();
            stack.push(val);
            stacks.add(stack);
        }
        else
            stacks.get(stacks.size() - 1).push(val);
    }
    
    public int pop() {
        return popAt(stacks.size() - 1);
    }
    
    public int popAt(int index) {
        if (index < 0 || index >= stacks.size())
            return -1;
        int val = stacks.get(index).pop();
        if (stacks.get(index).empty())
            stacks.remove(index);
        return val;
    }

}

/**
 * Your StackOfPlates object will be instantiated and called as such:
 * StackOfPlates obj = new StackOfPlates(cap);
 * obj.push(val);
 * int param_2 = obj.pop();
 * int param_3 = obj.popAt(index);
 */
