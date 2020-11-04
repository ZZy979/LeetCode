class Solution {
    // memo[i]：以箱子i为底的最大箱子堆高度
    private int[] memo;

    public int pileBox(int[][] box) {
		Arrays.sort(box, Comparator.comparing(b -> ((int[]) b)[2]).reversed());
        memo = new int[box.length];
        return createStack(box, -1, 0);
    }

    private int createStack(int[][] boxes, int bottomIndex, int k) {
        if (k >= boxes.length)
            return 0;
        // 以箱子k为底
        int heightWithBottom = 0;
        if (bottomIndex == -1 || canBeAbove(boxes[k], boxes[bottomIndex])) {
            if (memo[k] == 0)
                memo[k] = createStack(boxes, k, k + 1) + boxes[k][2];
            heightWithBottom = memo[k];
        }
        // 不以箱子k为底
        int heightWithoutBottom = createStack(boxes, bottomIndex, k + 1);
        return Math.max(heightWithBottom, heightWithoutBottom);
    }

    private boolean canBeAbove(int[] box1, int[] box2) {
        return box1[0] < box2[0] && box1[1] < box2[1] && box1[2] < box2[2];
    }

}
