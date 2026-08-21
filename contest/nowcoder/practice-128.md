# 牛客练习赛 128

> 复盘状态：D、E、F 未完成（原文标记为 `exc`）。

## C - Cidoai 的树上方案

### 基本信息

| 字段 | 内容 |
| --- | --- |
| 平台 | 牛客 |
| 题号 | 牛客练习赛 128 C |
| 原题链接 | [C - Cidoai 的树上方案](https://ac.nowcoder.com/acm/contest/88880/C) |
| 难度 / Rating | TODO |
| 知识点标签 | 树形 DP |

### 题意概括

给定一棵大小为 $n$ 的有标号有根树，以 $1$ 为根。求从树外引出一个点，并向树内任意连边，使构成的简单图不含三元环的方案数。答案对 $998244353$ 取模。

### 核心思路

$dfs(u,0/1)$ 表示节点 $u$ 及其子树有多少种选择方法，其中 $0/1$ 表示不选择或选择节点 $u$。

选择当前节点 $u$ 时，其子节点不能选择；不选择当前节点 $u$ 时，子节点可以选择或不选择。各子节点的选法数累乘，即得到 $dfs(u,0/1)$。

### 正确性说明

TODO：原文未提供完整的正确性说明。

### 复杂度

- 时间复杂度：TODO
- 空间复杂度：TODO

### 易错点

- TODO：原文未记录易错点。

### 代码

#### Java

```java
    static int n, mod = 998244353;
    static long memo[][];
    static List<Integer> adj[];
    public static void solve() throws IOException{     
        n = rd.nextInt();    
        adj = new ArrayList[n + 1];
        Arrays.setAll(adj, i -> new ArrayList<>());
        for(int i = 2; i <= n; i ++){
            int u = rd.nextInt();
            adj[u].add(i);
        }
        memo = new long[n + 1][2];
        for(int i = 1; i <= n; i ++) Arrays.fill(memo[i], -1);
        pw.println((dfs(1, 0) + dfs(1, 1)) % mod);
    }
    public static long dfs(int u, int t){
        if(memo[u][t] != -1) return memo[u][t];
        memo[u][0] = 1;
        memo[u][1] = 1;
        for(int v : adj[u]){
            memo[u][0] = memo[u][0] * (dfs(v, 0) + dfs(v, 1)) % mod;
            memo[u][1] = memo[u][1] * dfs(v, 0) % mod;
        }
        return memo[u][t];
    }
```

#### Python

TODO：原文未提供 Python 代码。

### 复盘与可迁移结论

- TODO：原文未记录复盘或可迁移结论。
