# Codeforces Div. 2 比赛记录

## [Educational Round 168 (Div. 2)](https://codeforces.com/contest/1997)

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

## [Round 963 (Div. 2)](https://codeforces.com/contest/1993)

[Problem - B - Codeforces](https://codeforces.com/contest/1993/problem/B)

给定一个由 n 个正整数组成的数组 a 。

在一次操作中，你可以选取任意一对索引 $(i,j)$，且 $a_i$ 和 $a_j$ 具有**不同的**奇偶性，然后用它们的和替换较小的那个。

求使数组中所有元素具有相同奇偶性所需的最少操作数。

> 思维、贪心

> 首先合并两个奇偶不一的数得到的一定是一个奇数，那么最终结果一定是将数组中所有偶数都变为奇数。
>
> 我们将合并操作理解为一个较大数吃掉较小数，产生一个新的合并的数。贪心地，尽量用奇数去吃掉偶数，这样会直接减少一个偶数；而用偶数去吃奇数不会减少偶数个数。
>
> 接下来我们去判断一个尽量大地奇数是否能够将所有偶数吃完。首先，如果数组中地最大值是奇数，那么毫无疑问它可以吃掉所有偶数，吃地次数等于偶数个数。若最大值不是奇数，我们就用最大的奇数从小到大地吃偶数，过程中维护它吃了偶数之后变大地值，直到不能再吃偶数。如果它不能将偶数吃完，也就是吃到不能再吃了也无法大于最大的偶数值。那么就需要用最大的偶数值与一个较小的奇数值造一个最大的奇数出来，将剩余偶数吃掉，这个过程用了偶数数量+1次操作

> $O(n)$

```java
import java.io.*;
import java.util.*;

public class Prac {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    public static void solve(){
        int n = sc.nextInt();
        int a[] = new int[n];
        int odd = 0, mxodd = 0;
        for(int i = 0; i < n; i ++) {
            a[i] = sc.nextInt();
            if(a[i] % 2 == 1) {
                odd ++;
                mxodd = Math.max(mxodd, a[i]);
            }
        }
        Arrays.sort(a);
        if(odd == 0) {
            pw.println(0);
            return;
        }
        if(a[n - 1] % 2 == 1) pw.println(n - odd);
        else{
            long sum = mxodd;
            for(int i = 0; i < n; i ++){
                if(a[i] % 2 == 0 && a[i] < sum) sum += a[i]; 
            }
            pw.println(sum > a[n - 1] ? n - odd : n - odd + 1);
        }
    }
    public static void main(String[] args) throws IOException {     
        int T = sc.nextInt();
        while(T --> 0) solve();
        pw.flush();pw.close();
    }
}

```

[Problem - C - Codeforces](https://codeforces.com/contest/1993/problem/C)

有一个由 n 个房间组成的公寓，每个房间的灯最初都是关着的。

为了控制这些房间的灯光，公寓的主人决定在房间里安装芯片，这样每个房间正好有一个芯片，芯片安装在不同的时间。具体来说，这些时间由数组 a1,a2,…,an 表示，其中 ai 是在 i /th房间安装芯片的时间(以分钟为单位)。

芯片安装后，每隔 kk 分钟就会改变房间的灯光状态--在 kk 分钟内打开灯光，然后在接下来的 kk 分钟内关闭灯光，再在接下来的 kk 分钟内重新打开灯光，以此类推。换句话说，芯片在 ai 、 ai+k 、 ai+2k 、 ai+3k 、 …… 分钟时改变 i /th房间的灯光状态。

公寓里所有房间最早亮灯的时刻是什么时候？

> 模拟？

> 求最早时刻所有灯都处于亮的状态。首先一定是在安装最后一个灯泡后出现这个时刻，且一定是出现在最后这个灯的第一个亮区间内。因为所有灯的周期是一样的，那么整体情况也会有一个周期且为$2k$，在最后这个灯的每个明亮区间内，所有灯的状态变化是一致的。如果第一个明亮区间没有出现全亮，就不可能出现全亮了。
>
> 我们求最后一个灯炮的第一个明亮区间和前面每个灯泡在这个时间区间内明亮区间的交集即可。

> $O(n\log n)$

```java
import java.io.*;
import java.util.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    public static void solve(){
        int n = sc.nextInt();
        int k = sc.nextInt();
        int a[] = new int[n];
        for(int i = 0 ; i < n; i ++) a[i] = sc.nextInt();
        Arrays.sort(a);
        int l = a[n - 1], r = a[n - 1] + k;
        for(int i = n - 2; i >= 0; i --){
            int x = (a[n - 1] - a[i]) / k;
            if(x % 2 == 0){
                r = Math.min(r, a[i] + x * k + k);
            }else{
                l = Math.max(l, a[i] + x * k + k);
            }
        }
        pw.println(l < r ? l : -1);
    }
    public static void main(String[] args) throws IOException {     
        int T = sc.nextInt();
        while(T --> 0) solve();
        pw.flush();pw.close();
    }
}

```



## [Educational Round 169 (Div. 2)](https://codeforces.com/contest/2004)

[Problem - D - Codeforces](https://codeforces.com/contest/2004/problem/D)

There are $n$ cities located on a straight line. The cities are numbered from $1$ to $n$.

Portals are used to move between cities. There are $4$ colors of portals: blue, green, red, and yellow. Each city has portals of two different colors. You can move from city $i$ to city $j$ if they have portals of the same color (for example, you can move between a "blue-red" city and a "blue-green" city). This movement costs $|i-j|$ coins.

Your task is to answer $q$ independent queries: calculate the minimum cost to move from city $x$ to city $y$.

> 记录每种颜色组合有哪些地方（map实现），对于$x、y$若能直接跳就直接跳，若不能则去寻找中转站。
>
> 若$[x+1,y-1]$中有中转站那么那么答案为$y-x$。这一步判断用**前缀和**实现。
>
> 再去可能的中转站中寻找位置在$[1,x-1]、[y + 1,n]$中最近的中转站，这一步用**二分查找**实现。

> TODO：补充实现并用样例验证。

## [Round 958 (Div. 2)](https://codeforces.com/contest/1988)

[Problem - C - Codeforces](https://codeforces.com/contest/1988/problem/C)

给定正整数 $n$. 构造**最长**的序列 $a=[a_1,a_2,\ldots,a_k]$ 满足:

- $a_i\le n$ for all $1\le i\le k$.
- $a$ 严格递增
- $a_i\,|\,a_{i-1}=n$ for all $2\le i\le k$, |代表按位异或

> 位运算， lowbit

> 注意到要序列**最长**，从最大数开始构造，最大那个数一定是$n$本身，次大值一定为$n - lowbit(n)$一次类推，可以构造出长度为$bitcount(n) + 1$的序列。

> $O(n + n\log n)$瓶颈在排序。

```java
import java.io.*;
import java.util.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    public static void solve(){
        long n = sc.nextLong();
        Vector<Long> ans = new Vector<>();
        long x = n;
        while(x > 0){
            long e = n - (x & -x);
            if(e != 0) ans.add(e);
            x -= (x & -x);
        }
        ans.add(n);
        Collections.sort(ans);
        pw.println(ans.size());
        for(long e : ans) pw.print(e + " ");
        pw.println();
    }
    public static void main(String[] args) throws IOException {
        int T = sc.nextInt();
        while(T --> 0){solve();}
        pw.flush();pw.close();
    }
}
```



## [Round 975 (Div. 2)](https://codeforces.com/contest/2019) (exc: D E F)

[Problem - C - Codeforces](https://codeforces.com/contest/2019/problem/C)

> 枚举答案
>
> 至少需要分成$m=\max(a_i)$组。枚举牌组的大小$i$，计算出需要分成多少组，分成$t=\max(m,\lceil \frac{sum}{i} \rceil )$，判断是否$t\times i\le sum+k$，满足则$i$合法。

```java
    static public void solve() throws IOException{
        int n = rd.nextInt();
        long k = rd.nextLong();
        long max = 0, sum = 0;
        for(int i = 0; i < n; i ++) {
            long x = rd.nextLong();
            max = Math.max(max, x);
            sum += x;
        }
        for(int i = n; i >= 1; i --){
            if(max * i <= sum + k && (sum + i - 1) / i * i <= sum + k){
                pw.println(i);
                return;
            }
        }
    }
```

