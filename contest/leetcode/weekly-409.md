# 第 409 场周赛（待补T4）

[3244. 新增道路查询后的最短距离 II - 力扣（LeetCode）](https://leetcode.cn/problems/shortest-distance-after-road-addition-queries-ii/description/)

给你一个整数 `n` 和一个二维整数数组 `queries`。

有 `n` 个城市，编号从 `0` 到 `n - 1`。初始时，每个城市 `i` 都有一条**单向**道路通往城市 `i + 1`（ `0 <= i < n - 1`）。

`queries[i] = [ui, vi]` 表示新建一条从城市 `ui` 到城市 `vi` 的**单向**道路。每次查询后，你需要找到从城市 `0` 到城市 `n - 1` 的**最短路径**的**长度**。

所有查询中不会存在两个查询都满足 `queries[i][0] < queries[j][0] < queries[i][1] < queries[j][1]`。

返回一个数组 `answer`，对于范围 `[0, queries.length - 1]` 中的每个 `i`，`answer[i]` 是处理完**前** `i + 1` 个查询后，从城市 `0` 到城市 `n - 1` 的最短路径的*长度*。

> 区间并查集

```java
class Solution {
    int p[];
    public int[] shortestDistanceAfterQueries(int n, int[][] q) {
        p = new int[n];
        int ans[] = new int[q.length];
        for(int i = 0; i < n; i ++) p[i] = i;
        int cnt = n - 1;
        for(int i = 0; i < q.length; i ++){
            int l = q[i][0];
            int r = q[i][1] - 1;
            for(int j = find(l); j < r; j = find(j + 1)){
                p[j] = find(r);
                cnt --;
            }
            ans[i] = cnt;
        }
        return ans;
    }
    public int find(int x){
        if(p[x] != x) p[x] = find(p[x]);
        return p[x];
    }
}
```

