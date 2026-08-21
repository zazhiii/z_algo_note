# 牛客小白月赛96

[B-最少操作次数](https://ac.nowcoder.com/acm/contest/84528/B)

有一个长度为$n$的字符串$S$，仅包含$0$和$1$两种字符。
每次可以选择两个索引i和$j(1\leq i＜j\leq n)$，并满足以下条件之一：
 1.如果区间 $[i,j]$ 中 $1$ 的数量大于 $0$ 的数量，可以把此区间的所有数字都变成 $1$。

 2.如果区间$[i,j]$ 中 $0$ 的数量大于 $1$ 的数量，可以把此区间的所有数字都变成 $0$。

把整个串变成全 $0$ 或者全 $1$ 的最少操作次数，如果无解，输出$−1$。

> 分类讨论、贪心

> 当$n=1$，显然答案为$0$。
>
> 当$n=2$，两个字母相同答案为$0$，反之为$-1$。
>
> 当$n\ge3$，要操作次数最少，每次操作越多数越好。当序列中$1$数量与$0$数量相同时则需要操作两次。不同时只需$1$次操作即可。若其中一个数量为$0$答案为$0$。
>
> $O(n)$

```java
import java.io.*;
import java.util.*;
public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    public static void main(String[] args) throws Exception {
        int n = sc.nextInt();
        String s = sc.next();
        if(n == 1){
            pw.println(0);
        }else if(n == 2){
            if(s.charAt(0) == s.charAt(1)) pw.println(0);
            else pw.print(-1);
        }else{
            int a = 0, b  = 0;
            for(int i = 0; i < n; i ++){
                if(s.charAt(i) == '1') a ++;
                else b ++;
            }
            if(a == 0 || b == 0) pw.print(0);
            else if(a == b) pw.print(2);
            else pw.print(1);
        }
        pw.flush();
        pw.close(); 
    }
}
```

[C-最多数组数量)](https://ac.nowcoder.com/acm/contest/84528/C)

一个山峰数组定义为由三个元素组成$[a1,a2,a3]$,满足 $a_1＜a_2$ 且 $a_2＞a_3$。

有一个长度为 $n$ 的数组 $P$，他将选择两个索引 $i,j(1≤i＜j＜n)$,然后分成三个非空连续的子数组，即$b_1=\sum_{k=1}^{k=i} P_k,b_2=\sum_{k=i+1}^{k=j} P_k,b_3=\sum_{k=j+1}^{k=n} P_k$，满足$[b_1,b_2,b_3]$是一个山峰数组。

共有多少个不同的 $(i,j)$ 可以满足条件.

> 前缀和+二分

> 枚举第一个区间的右端点$[1,n-1]$，二分查找满足山峰数组的第二个区间的**最小**右端点$i$（若存在），累加所有$n - 1 - i + 1 = n-i$。
>
> 所有的区间和用前缀和数组计算。
>
> $O(n\log n)$

```java
import java.io.*;
import java.util.*;
public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static int n;
    static long ans = 0, a[], s[];
    public static void main(String[] args) throws Exception {
        n = sc.nextInt();
        a = new long[n + 1];
        s = new long[n + 1];
        for(int i = 1; i <= n; i ++){
            a[i] = sc.nextInt();
            s[i] = s[i - 1] + a[i];
        }
        for(int i = 1; i <=n - 2; i ++){
            long lsum = s[i];
            int l = i + 1, r = n - 1, idx = -1;
            while(l <= r){
                int m = (l + r) >>> 1;
                if(s[m] - s[i] > lsum && s[m] - s[i] > s[n] - s[m]){
                    idx = m;
                    r = m - 1;
                }else{
                    l = m + 1;
                }
            }
            if(idx != -1) ans += n - 1 - idx + 1;
        }
        pw.println(ans);
        pw.flush();
        pw.close(); 
    }

}
```

[D-最小连通代价](https://ac.nowcoder.com/acm/contest/84528/D)

有 n 个结点，第 i 个结点的权值为 $A_i$。 初始时都为孤立的点，互不连通。

 现在需要加若干条无向边，使得所有点构成一张无向连通图。

 我们定义在两个结点之间加边的代价为：如果两个点的权值都是偶数或者都是奇数，代价为 a。否则为 b。

 算出所有点构成一张无向连通图的最小代价之和。

> 分类讨论

>  讨论odd和even的个数，a和b的正负。讨论情况比较多。  
>
>  **又犯了每组数据的变量不重新初始化的错误。。。😓**    
>
>  $O(Tn)$     

```java
import java.io.*;
import java.util.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static int T, n;
    static long  a, b;
    public static void main(String[] args) throws Exception {
        T = sc.nextInt();
        while(T --> 0){
            n = sc.nextInt();
            a = sc.nextLong();
            b = sc.nextLong();
            long o = 0, e = 0;
            for(int i = 0; i < n; i ++){
                int x = sc.nextInt();
                if(x % 2 == 0) e ++;
                else o ++;
            }
            long ans = 0;
            if(a < 0 && b < 0){
                ans += a * (e - 1) * e / 2;
                ans += a * (o - 1) * o / 2;
                ans += b * e * o;
            }else if(a < 0 && b >= 0){
                ans += a * (e - 1) * e / 2;
                ans += a * (o - 1) * o / 2;
                if(e > 0 && o > 0) ans += b;
            }else if(a >= 0 && b < 0){
                //may only odd or even
                if(e == 0 || o == 0){
                    ans = (n - 1) * a;
                }else{
                    ans = b * e * o;
                }
            }else{
                if(e == 0 || o == 0) ans = a * (n - 1);
                else ans = a < b ? (n - 2) * a + b : (n - 1) * b; 
            }
            pw.println(ans);
        }
        pw.flush();pw.close(); 
    }
}
```

