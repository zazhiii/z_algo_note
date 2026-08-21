# Round 957 (Div. 3)

[C - Gorilla and Permutation](https://codeforces.com/contest/1992/problem/C)

给出$n, m,k \ (m<k)$。构造$n$的排列。

$g(i)$表示前$i$个数中小于等于$m$的数的和。

$f(i)$表示前$i$个数中大于等于$k$的数的和。

构造$n$的排列使得$\sum_{i=1}^nf(i)-\sum_{i=1}^ng(i)$最大。

> 贪心、构造

> 式中$f(i)$取得正，$g(i)$取的负。所以将大于等于$k$的数中较大的尽量往前方放，将小于等于$m$中的数的较大者尽量往后放。最终构造出：$[n,n-1,...,k,...,1,2,...,m]$
>
> **直接输出即可**
>
> $O(n)$

```java
import java.io.*;
import java.util.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    public static void solve(){
        int n, m, k;
        n = sc.nextInt();
        m = sc.nextInt();
        k = sc.nextInt();
        for(int i = n; i >= m + 1; i --) pw.print(i + " ");
        for(int i = 1; i <= m; i ++) pw.print(i + " ");
        pw.println();
    }
    public static void main(String[] args) throws IOException {
        int T = sc.nextInt();
        while(T --> 0) solve();
        pw.flush();pw.close();
    }
}
```

[D - Test of Love](https://codeforces.com/contest/1992/problem/D)

给出$n,m,k$。表示河道长度，最远跳跃距离，最多游泳距离。

河道用$L, C, W$表示木桩，鳄鱼，水。

在木桩上和起点能跳跃，在水中能游泳，不能在有鳄鱼的地方。

是否能在$k$次游泳之内从起点$0$到达终点$n+1$

> dp

> 1. $dp[i]$：到第$i$个位置最少需要游泳多少距离
> 2. 初始化$dp[0]=0, dp[i] =inf(i>0)$
> 3. 状态转移（两种方式）：
>      1. 可以从前面有木桩的地方或起点(距离$m$以内)或前一格有水的地方转移到当前位置
>      2. 若当前为起点或木桩，可以从当前状态转移到前面(距离$m$以内)地方。
> 4. 判断$dp[n+1]$是否小于$k$即可。

```java
import java.io.*;
import java.util.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    public static void solve(){
        int n, m, k, inf = (int)2e9;
        n = sc.nextInt();
        m = sc.nextInt();
        k = sc.nextInt();
        char[] c = sc.next().toCharArray();
        int dp[] = new int[n + 2];
        Arrays.fill(dp, inf);
        dp[0] = 0;
        for(int i = 1; i <= n + 1; i ++){
            if(i <= n && c[i - 1] == 'C') continue;
            dp[i] = dp[i - 1] + 1;
            for(int j = 1; j <= m && i - j >= 0; j ++){
                if(i - j == 0 || c[i - j - 1] == 'L') dp[i] = Math.min(dp[i], dp[i - j]);
            }
        }
        pw.println(dp[n + 1] <= k ? "YES" : "NO");
    }
    public static void main(String[] args) throws IOException {
        int T = sc.nextInt();
        while(T --> 0) solve();
        pw.flush();pw.close();
    }
}
---------------------------------------------------------------------
import java.io.*;
import java.util.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    public static void solve(){
        int n, m, k, inf = (int)2e9;
        n = sc.nextInt();
        m = sc.nextInt();
        k = sc.nextInt();
        char[] c = sc.next().toCharArray();
        int dp[] = new int[n + 2];
        Arrays.fill(dp, inf);
        dp[0] = 0;
        for(int i = 0; i < n + 1; i ++){
            if(dp[i] == inf) continue;
            if(i == 0 || c[i - 1] == 'L'){
                for(int j = 1; j <= m && i + j <= n + 1; j ++){
                    dp[i + j] = Math.min(dp[i], dp[i + j]);
                }
            }else if(c[i - 1] == 'W'){
                dp[i + 1] = Math.min(dp[i] + 1, dp[i + 1]);
            }
        }
        pw.println(dp[n + 1] <= k ? "YES" : "NO");
    }
    public static void main(String[] args) throws IOException {
        int T = sc.nextInt();
        while(T --> 0) solve();
        pw.flush();pw.close();
    }
}

```

