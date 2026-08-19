# 最短路题单

## Dijkstra

[3286. 穿越网格图的安全路径 - 力扣（LeetCode）](https://leetcode.cn/problems/find-a-safe-walk-through-a-grid/description/)

[LeetCode find-minimum-time-to-reach-last-room-i](https://leetcode.cn/problems/find-minimum-time-to-reach-last-room-i)



## 分图层最短路

[洛谷 P4568](https://www.luogu.com.cn/problem/P4568)

> 每个节点视作有`k`个状态，整个图相当于变成了`k`层。`d[v][k]`表示到节点`v`用了`k`次免费的最小花费，然后再跑$dijkstra$，对免费或不免费分别做两次松弛操作

[Codeforces 2014E](https://codeforces.com/contest/2014/problem/E)

>每个节点视作骑马和不骑马两个状态，视作两层图，`d[u][k]`表示到节点`u`且是否(1/0)时骑马过来的。再跑dijkstra，做松弛操作时，分成三种情况讨论即可。跑两次dijkstra，算出从1出发到各个点的花费和从n出发到各个点的花费，答案为到某个点会和两人花费的较大值的最小值。

[AtCoder abc395_e](https://atcoder.jp/contests/abc395/tasks/abc395_e)

> 定义`d[n + 1][2]`，`d[i][0/1]`代表到节点`i`且当前状态是没反转/反转的最短路程，跑dijkstra。
