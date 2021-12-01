// 有序映射
class SummaryRanges {
    private TreeMap<Integer, Integer> intervals;

    public SummaryRanges() {
        intervals = new TreeMap<>();
    }
    
    public void addNum(int val) {
        // interval0 = [l0, r0] 使得l0最大且满足l0 <= val
        Map.Entry<Integer, Integer> interval0 = intervals.floorEntry(val);
        // interval1 = [l1, r1] 使得l1最小且满足l1 > val
        Map.Entry<Integer, Integer> interval1 = intervals.higherEntry(val);
        if (interval0 != null && interval0.getKey() <= val && val <= interval0.getValue()) {
            // l0 <= val <= r0
            return;
        }
        boolean leftAside = interval0 != null && val == interval0.getValue() + 1;  // val == r0 + 1
        boolean rightAside = interval1 != null && val == interval1.getKey() - 1;  // val == l1 - 1
        if (leftAside && rightAside) {
            intervals.put(interval0.getKey(), interval1.getValue());
            intervals.remove(interval1.getKey());
        }
        else if (leftAside) {
            intervals.put(interval0.getKey(), interval0.getValue() + 1);
        }
        else if (rightAside) {
            intervals.remove(interval1.getKey());
            intervals.put(val, interval1.getValue());
        }
        else {
            intervals.put(val, val);
        }
    }
    
    public int[][] getIntervals() {
        return intervals.entrySet().stream()
            .map(entry -> new int[] {entry.getKey(), entry.getValue()})
            .toArray(int[][]::new);
    }
}

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * SummaryRanges obj = new SummaryRanges();
 * obj.addNum(val);
 * int[][] param_2 = obj.getIntervals();
 */
