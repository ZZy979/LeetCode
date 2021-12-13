class MyCalendar {
    private TreeSet<int[]> events;

    public MyCalendar() {
        events = new TreeSet<>((a, b) -> {
            if (a[1] <= b[0])
                return -1;
            else if (a[0] >= b[1])
                return 1;
            else
                return 0;
        });
    }
    
    public boolean book(int start, int end) {
        return events.add(new int[] {start, end});
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
 * boolean param_1 = obj.book(start,end);
 */
