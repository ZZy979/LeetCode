class SortedStack {
    private Stack<Integer> mainStack, subStack;

    public SortedStack() {
        mainStack = new Stack<>();
        subStack = new Stack<>();
    }
    
    public void push(int val) {
        while (!mainStack.empty() && mainStack.peek() < val)
            subStack.push(mainStack.pop());
        while (!subStack.empty() && subStack.peek() > val)
            mainStack.push(subStack.pop());
        mainStack.push(val);
    }
    
    public void pop() {
        subToMain();
        if (!mainStack.empty())
            mainStack.pop();
    }
    
    public int peek() {
        subToMain();
        return mainStack.empty() ? -1 : mainStack.peek();
    }
    
    public boolean isEmpty() {
        return mainStack.empty() && subStack.empty();
    }

    private void subToMain() {
        while (!subStack.empty())
            mainStack.push(subStack.pop());
    }

}

/**
 * Your SortedStack object will be instantiated and called as such:
 * SortedStack obj = new SortedStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.isEmpty();
 */
