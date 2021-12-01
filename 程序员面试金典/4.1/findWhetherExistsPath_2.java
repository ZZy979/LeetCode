// 起点可达；可达顶点的邻接点可达
class Solution {
    public boolean findWhetherExistsPath(int n, int[][] graph, int start, int target) {
        boolean[] reachable = new boolean[n];
        reachable[start] = true;
        for(int[] edge : graph)
            if(reachable[edge[0]])
                reachable[edge[1]] = true;
        return reachable[target];
    }
}
