# 第 139 场双周赛（exc：T3、T4)

T2  [3286. 穿越网格图的安全路径 - 力扣（LeetCode）](https://leetcode.cn/problems/find-a-safe-walk-through-a-grid/description/)

给一个`01`网格，求从`(0, 0)`位置到`(n, m)`位置经过的路径上的值能否小于`h`

*   `1 <= m, n <= 50`

> dijkstra

```java
// dijkstra
class Solution {
    int a[][], n, m, d[][];
    boolean vis[][];
    int[] dx = {1, -1, 0, 0}, dy = {0, 0, 1, -1};
    public boolean findSafeWalk(List<List<Integer>> grid, int h) {
        n = grid.size(); m = grid.get(0).size();
        a = new int[n][m];
        d = new int[n][m];
        vis = new boolean[n][m];
        for(int i = 0; i < n; i ++) for(int j = 0; j < m; j ++) a[i][j] = grid.get(i).get(j);
        for(int i = 0; i < n; i ++) Arrays.fill(d[i], (int)1e9);
        Queue<int[]> que = new PriorityQueue<>((o1, o2) -> o1[2] - o2[2]);
        d[0][0] = a[0][0];
        que.add(new int[]{0, 0, d[0][0]});
        while(!que.isEmpty()){
            int p[] = que.poll();
            int x = p[0]; int y = p[1]; int k = p[2];
            if(vis[x][y]) continue;
            vis[x][y] = true;
            for(int i = 0; i < 4; i ++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                if(nx >= 0 && nx < n && ny >= 0 && ny < m && !vis[nx][ny]){
                    if(d[nx][ny] > d[x][y] + a[nx][ny]){
                        d[nx][ny] = d[x][y] + a[nx][ny];
                        que.add(new int[]{nx, ny, d[nx][ny]});
                    }
                }
            } 
        }
        return d[n - 1][m - 1] < h;
    }
}
```

