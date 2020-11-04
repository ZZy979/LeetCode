class Solution {
    // memo[i]：以箱子i为底的最大箱子堆高度
    private int[] memo;

    public int pileBox(int[][] box) {
		Arrays.sort(box, Comparator.comparing(b -> ((int[]) b)[2]).reversed());
        memo = new int[box.length];
        int maxHeight = 0;
        for (int i = 0; i < box.length; ++i) {
            int height = createStack(box, i);
            maxHeight = Math.max(maxHeight, height);
        }
        return maxHeight;
    }

    private int createStack(int[][] boxes, int bottomIndex) {
        if (bottomIndex < boxes.length && memo[bottomIndex] > 0)
            return memo[bottomIndex];
        int maxHeight = 0;
        for (int i = bottomIndex + 1; i < boxes.length; ++i)
            if (canBeAbove(boxes[i], boxes[bottomIndex])) {
                int height = createStack(boxes, i);
                maxHeight = Math.max(maxHeight, height);
            }
        maxHeight += boxes[bottomIndex][2];
        memo[bottomIndex] = maxHeight;
        return maxHeight;
    }

    private boolean canBeAbove(int[] box1, int[] box2) {
        return box1[0] < box2[0] && box1[1] < box2[1] && box1[2] < box2[2];
    }

}
