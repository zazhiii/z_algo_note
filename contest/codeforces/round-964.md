# [Round 964 (Div. 4)](https://codeforces.com/contest/1999) （exc：G1 G2）

[Problem - 1999E - Codeforces](https://codeforces.com/problemset/problem/1999/E)

Ivy 在黑板上写下了在 $l$ 到 $r$ 之间的所有整数。

在一次运算中，她做了以下操作：

- 在黑板上选出任意两个数字 $x$ 和 $y$ ，将它们擦掉，然后在它们的位置上写下数字 $3x$ 和 $\lfloor \frac{y}{3} \rfloor$ 。(这里的 $\lfloor x\rfloor$ 表示取整，即四舍五入到最接近的整数）。

要使黑板上的所有数字都等于 $0$ ，Ivy 最少需要进行多少次运算？可以证明一定有解。

第一行包含一个正整数 $t$ ( $1 \leq t \leq 10^4$ )，表示测试用例的数量。

对于每个测试用例，仅一行包含两个正整数 $l$ 和 $r$ ( $1 \leq l <  r \leq 2 \cdot 10^5$ )。

> 预处理

> 首先先把一个数变为$0$，再用这个数将其他数变为$0$。
>
> 预处理$1\sim2\times10^5$之间的每一个数需要除几次能为$0$，在$3^k\sim 3^{k+1}-1$之间的数需要除$k+1$次能为$0$
>
> 答案为所有数变为$0$的操作次数，再加上最小的那个数变为$0$的操作次数

```java
    static long pow3[] = new long[15];
    static long cnt[] = new long[(int)2e5 + 1];
    static long pre[] = new long[(int)2e5 + 1];
    public static void init(){
        pow3[0] = 1;
        for(int i = 1; i < 15; i ++) pow3[i] = pow3[i - 1] * 3;
        int k = 0;
        for(int i = 1; i < (int)2e5 + 1; i ++){
            if(i >= pow3[k] && i <= pow3[k + 1] - 1){
                cnt[i] = k + 1;
            }else{
                k ++;
                cnt[i] = k + 1; 
            }
            pre[i] = pre[i - 1] + cnt[i];
        }
    }
    public static void solve(){
        int l = sc.nextInt();
        int r = sc.nextInt();
        pw.println(pre[r] - pre[l - 1] + cnt[l]);
    }
```

[Problem - F - Codeforces](https://codeforces.com/contest/1999/problem/F)

Arul has a **binary** array$^{\text{∗}}$ $a$ of length $n$.

He will take all subsequences$^{\text{†}}$ of length $k$ ($k$ is odd) of this array and find their median.$^{\text{‡}}$

What is the sum of all these values?

As this sum can be very large, output it modulo $10^9 + 7$. In other words, print the remainder of this sum when divided by $10^9 + 7$.

$^{\text{∗}}$A binary array is an array consisting only of zeros and ones.

$^{\text{†}}$An array $b$ is a subsequence of an array $a$ if $b$ can be obtained from $a$ by the deletion of several (possibly, zero or all) elements. Subsequences **don't** have to be contiguous.

$^{\text{‡}}$The median of an array of odd length $k$ is the $\frac{k+1}{2}$\-th element when sorted.

> 组合数

> 要使得$k$子序列中的中位数为$1$，那么其中至少有$\lceil \frac{k}{2} \rceil$个$1$，
>
> 从所有$1$中选$i(\lceil \frac{k}{2} \rceil\le i\le k)$个$1$出来，再从所有$0$中选$k-i$个$0$出来。
>
> $\sum^{k}_{i=\lceil \frac{k}{2} \rceil}C_{one}^{i}\times C_{zero}^{k-i}$

```java
import java.io.*;
import java.util.*;
public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(System.out);

    static int mod = (int)1e9 + 7;
    static int max = (int)2e5 + 10;
    static long f[] = new long[max];
    static long invf[] = new long[max];

    public static long qpow(long a, long n){
        long ans = 1;
        while(n > 0){
            if(n % 2 == 1) ans = ans * a % mod;
            a = a * a % mod;
            n >>>= 1;
        }
        return ans;
    }
    public static void init(){
        f[0] = invf[0] = 1;
        for(int i = 1; i < max; i ++){
            f[i] = f[i - 1] * i % mod;
            invf[i] = invf[i - 1] * qpow(i, mod - 2) % mod;
        }
    }
    public static long C(int a, int b){
        if(b > a) return 0;
        return f[a] * invf[b] % mod * invf[a - b] % mod;
    }
    public static void solve(){
        int n = sc.nextInt();
        int k = sc.nextInt();
        int zero = 0, one = 0;
        for(int i = 0; i < n; i ++){
            int x = sc.nextInt();
            if(x == 1) one ++;
            else zero ++;
        }
        long ans = 0;
        //c[one][i] * c[zero][k - i];
        for(int i = k / 2 + 1; i <= k; i ++){
            ans = (ans + C(one, i) * C(zero, k - i)) % mod;
        }
        pw.println(ans);
    }
    public static void main(String[] args) throws IOException {
        int T = sc.nextInt();
        init();
        while(T --> 0) solve();
        pw.flush();
    }   
}
```

