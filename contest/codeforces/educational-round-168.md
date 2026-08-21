# [Educational Round 168 (Div. 2)](https://codeforces.com/contest/1997)

[Problem - D - Codeforces](https://codeforces.com/contest/1997/problem/D)

给你一棵有根的树，由 $n$ 个顶点组成。树上的顶点从 $1$到 $n$ 编号，根是顶点 $1$ 。第 $i$ 个顶点上的值为 $a_i$。

你可以执行以下操作任意次(可以为零次):选择一个至少有一个子顶点的顶点 $v$; 将 $a_v$ 增加 $1$ 并且对于 $v$ 的子树中的所有顶点 $u$ 将 $a_u$ 减少 $1$ (除了 $v$ 本身)。但是，在每次操作之后，所有顶点上的值都应该是非负的。

你的任务是使用前面提到的运算来计算写在根上的最大可能值。

 $n$ 之和不超过 $ 2 \times 10^5 $。

> 二分答案（还有其他做法）

> 如何检验二分的答案是否合法？，dfs访问除了根节点的每个节点，如果该节点的值足够贡献出答案则继续往后搜索，如果不够贡献答案就需要向其子树借相差的值，即子树需要贡献更多答案。就这样一直推算到叶子节点，因为叶子节点无法借答案，若其值不足以贡献其应该贡献的答案那么这个二分的值就是不合法的。如果所有叶子节点都足以贡献其应该贡献的值，那么这个二分的值就是合法的。现在找出最大的合法的值就是答案。
>
> **注意**：在dfs中可能会爆long，需要贡献的答案到一定的值剩余节点就不可能能够支付了，即使退出。

> $O(n\times\log V) V为二分范围$

```java
import java.io.*;
import java.util.*;

public class Prac {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static int n, a[];
    static Vector<Integer>[] adj;
    public static void solve(){
        n = sc.nextInt();
        a = new int[n + 1];
        adj = new Vector[n + 1];
        Arrays.setAll(adj, i -> new Vector<>());
        for(int i = 1; i <= n; i ++) a[i] = sc.nextInt();
        for(int i = 2; i <= n; i ++){
            int u = sc.nextInt();
            adj[u].add(i);
        }
        int l = 0, r = (int)2e9, ans = 0;
        while(l <= r){
            int m = (l + r) >>> 1;
            if(check(m)){
                ans = m;
                l = m + 1;
            }else{
                r = m - 1;
            }
        }
        pw.println(ans);
    }
    static boolean f;
    static long lim = (long)1e10;
    private static boolean check(int m) {
        f = true;
        for(int v : adj[1]){
            dfs(v, m - a[1]);
        }
        return f;
    }
    private static void dfs(int u, long need) {
        if((adj[u].isEmpty() && a[u] < need) ||need > lim){
            f = false;
            return;
        }
        if(a[u] < need) need += (need - a[u]);
        for(int v : adj[u]){
            dfs(v, need);
        }
    }
    public static void main(String[] args) throws IOException {
        int T = sc.nextInt();
        while(T --> 0) solve();
        pw.flush();pw.close();
    }
}
```

