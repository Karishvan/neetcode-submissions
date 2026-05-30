class MinStack {
    private ArrayList<Integer> s;
    private ArrayList<Integer> minStack;
    
    public MinStack() {
        s = new ArrayList<>();
        minStack = new ArrayList<>();
    }
    
    public void push(int val) {
        s.add(val);
        if (minStack.size() == 0){
            minStack.add(val);
        } else if (val < minStack.get(minStack.size()-1)) {
            minStack.add(val);
        } else {
            minStack.add(minStack.get(minStack.size()-1));
        }
    }
    
    public void pop() {
        s.remove(s.size()-1);
        minStack.remove(minStack.size()-1);
    }
    
    public int top() {
        return s.get(s.size()-1);
    }
    
    public int getMin() {  
        return minStack.get(minStack.size()-1);
        
    }
}
