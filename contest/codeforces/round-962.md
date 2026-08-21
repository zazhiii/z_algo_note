# [Round 962 (Div. 3)](https://codeforces.com/contest/1996)

[Problem - C - Codeforces](https://codeforces.com/contest/1996/problem/C)

给你两个字符串 $a$ 和 $b$ 长度为 $n$。对于 $q$  次询问。

每次询问，给定 $l$ 和 $r$. 在一次操作中可以选择一个 $i$ ($l \leq i \leq r$) 使 $a_i$ 变为任何一个字母. 输出最小操作次数使得 $\texttt{sorted(a[l..r])} = \texttt{sorted(b[l..r])}$. 

> 前缀和

> 意思就是使区间$l\sim r$中每一种字母的个数变为相等。用$26$个前缀和数组记录每个字母在该区间的数量，计算两个字符串在该区间的每个字母数量的差值的总和。答案为总差值的一半。（改一个字母可以消除两点差值）

> $O(T\times26\times(n + q))$

```java
import java.io.*;
import java.util.*;

public class Prac {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    
    static int n, q, pre1[][], pre2[][];
    static char a[], b[];
    public static void solve(){
        n = sc.nextInt();
        q = sc.nextInt();
        a = sc.next().toCharArray();
        b = sc.next().toCharArray();
        pre1 = new int[n + 1][26];
        pre2 = new int[n + 1][26];
        for(int i = 1; i <= n; i ++){
            for(int j = 0; j < 26; j ++){
                pre1[i][j] = pre1[i - 1][j];
                pre2[i][j] = pre2[i - 1][j];
            }
            pre1[i][a[i - 1] - 'a'] ++;
            pre2[i][b[i - 1] - 'a'] ++;
        }
        while(q --> 0){
            long ans = 0;
            int l = sc.nextInt();
            int r = sc.nextInt();
            l --;
            for(int i = 0; i < 26; i ++){
                ans += Math.abs(pre1[r][i] - pre1[l][i] - (pre2[r][i] - pre2[l][i]));
            }
            pw.println(ans / 2);
        }
    }
    public static void main(String[] args) throws IOException {
        int T = sc.nextInt();
        while(T --> 0) solve();
        pw.flush();pw.close();
    }
}
```

[Problem - D - Codeforces](https://codeforces.com/contest/1996/problem/D)

给定 $n$ 和 $x$, 寻找正整数 ($a,b,c$) 满足 $ab + ac + bc \le n$ and $a + b + c \le x$.

注意顺序 (e.g. ($1, 1, 2$) and ($1, 2, 1$) 被视为不同) 且 $a$, $b$, $c$ 严格大于$0$.

> 枚举

> 先枚举$a$，再枚举$b$，再计算$c$的个数。
>
> 由于$a,b,c$为正整数，所以$1\le a\le \min(x-2,\frac{n -1}{2})$
>
> 当$a$已确定，那么$b$的范围也随之缩小$1\le b\le\min (x-a-1,\frac{n-a}{a+1})$
>
> 对于每一对已经确定的$a和b$，范围$1\le c \le \min(x-a-b,\frac{n-ab}{a+b})$中的$c$都满足条件。即对于每一个确定的$a和b$都有$\min(x-a-b,\frac{n-ab}{a+b})$个$c$满足条件。累加这些$c$的数量即为答案。

> $O(???)$

```java
import java.io.*;
import java.util.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    
    static int n, x;
    public static void solve(){
        n = sc.nextInt();
        x = sc.nextInt();
        long ans = 0;
        for(int a = 1; a <= Math.min(x - 2, (n - 1) / 2); a ++){
            for(int b = 1; b <= Math.min(x - a - 1, (n - a) / (a + 1)); b ++){
                ans += Math.min(x - a - b, (n - a * b) / (a + b));
            }
        }
        pw.println(ans);
    }
    public static void main(String[] args) throws IOException {
        int T = sc.nextInt();
        while(T --> 0) solve();
        pw.flush();pw.close();
    }
}
```

[Problem - E - Codeforces](https://codeforces.com/contest/1996/problem/E)

给你一个长度为 $n$的二进制字符串 $s$

求出有多少种 $(l, r)$ $(1 \leq l \leq r \leq n)$， $(x, y)$ $(l \leq x \leq y \leq r)$ 子串 $s_xs_{x+1}...s_y$.中$0,1$数量相同。

> 前缀和，

> 一段$1$和$0$数量相等的字串，设左右端点为$l,r$（从$1$开始）, 对答案的贡献数量为$l\times (n-r+1)$。
>
> 去枚举这样的区间是$n^2$的复杂度，现在问题变为如何线性地计算出所有这样的子串的贡献。
>
> 用前缀和数组$pre$记录$1,0$的个数，用$1$表示$'1'$，$-1$表示$'0'$。对于这样的字串对应$pre[r]-pre[l-1]=0$
>
> 即在该数组中$l-1$位置和$r$位置的数是一样的。
>
> 遍历前缀和数组，对于当前位置，它可能是区间的左端点，也可能是右端点。我们计算它为右端点时对答案的贡献，对于前面每一个左端点$l$我们都要计算一次$l\times (n-r+1)$，所以我们考虑将前面左端点$l$累加起来再与$n-r+1$相乘。这样就能线性地算出总答案了。
>
> 我们用$Map$存当前位置对应的左端点的总和。
>
> 注意：0位置也要算进去（$pre$从1开始的）。

> $O(T\times n)$

```java
import java.io.*;
import java.util.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static int n, pre[], mod = (int)1e9 + 7;
    public static void solve(){
        char c[] = sc.next().toCharArray();
        Map<Integer, Long> map = new HashMap<>();
        n = c.length;
        pre = new int[n + 1];
        for(int i = 1; i <= n; i ++){
            pre[i] = pre[i - 1] + (c[i - 1] == '1' ? 1 : -1);
        }
        long ans = 0;
        map.put(0, 1l);
        for(int i = 1; i <= n; i ++){
            long preSum = map.getOrDefault(pre[i],0l);
            ans = (ans + 1l * preSum * (n - i + 1) % mod) % mod;
            map.put(pre[i], preSum + i + 1);
        }
        pw.println(ans);
    }
    public static void main(String[] args) throws IOException {
        int T = sc.nextInt();
        while(T --> 0) solve();
        pw.flush();pw.close();
    }
}
```

## [F. Bomb](https://codeforces.com/contest/1996/problem/F)（待补）

 给你两个长度为 $n$ 的数组 $a$ 和 $b$ 。最初，您的分数是 $0$ 。在一次操作中，您可以选择一个整数 $i$ 并将 $a_i$ 添加到您的分数中。然后，您必须设置 $a_i$ = $\max(0, a_i - b_i)$ 。

在 $k$ 次操作后，您能获得的最高分数是多少？

```java
import java.io.*;
import java.util.*;

public class Prac {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static int n, k, a[], b[];
    public static void solve(){
        n = sc.nextInt();
        k = sc.nextInt();
        a = new int[n];
        b = new int[n];
        for(int i = 0; i < n; i ++) a[i] = sc.nextInt();
        for(int i = 0; i < n; i ++) b[i] = sc.nextInt();
        int l = 0, r = (int)1e9 + 1, x = 0;
        while(l <= r){
            int m = (l + r) >>> 1;
            if(get(m)[0] <= k){
                x = m;
                r = m - 1;
            }else{
                l = m + 1;
            }
        }
        long p[] = get(x);
        // pw.print(x + " ");
        long cnt = p[0];
        long sum = p[1];
        if(x > 0){
            sum += (k - cnt) * (x - 1);
        }
        pw.println(sum);
    }
    private static long[] get(int m) {
        long cnt = 0;
        long sum = 0;
        for(int i = 0; i < n; i ++){
            if(a[i] >= m) {
                long t = (a[i] - m) / b[i] + 1;// times
                cnt += t;
                sum += a[i] * t - (t - 1) * t / 2 * b[i];
            }
        }
        return new long[]{cnt, sum};
    }
    public static void main(String[] args) throws IOException {
        int T = sc.nextInt();
        while(T --> 0) solve();
        pw.flush();pw.close();
    }
}
```

