# ✅牛客周赛 Round 60

[D-我们N个真是太厉害了_牛客周赛 Round 60 (nowcoder.com)](https://ac.nowcoder.com/acm/contest/90070/D)

给定$n$个数$a_1,a_2,...,a_n$，能否选取其中一些数加起来表示出$1\sim n$的每一个数。若不能输出最小的不能表示的数，若能输出`Cool!`$2\le n\le10^5$

> 用`dp[i]`表示前`i`个数能表示到的最大范围数。对于`a[i]`如果`a[i] <= dp[i - 1] + 1`那么就能无缝衔接上`dp[i - 1]`一直到`dp[i - 1] + a[i]`，如果`a[i] > dp[i - 1] + 1`那么`dp[i - 1] + 1` 这个数就永远凑不出来了。

```java
    public static void solve() throws IOException{     
        int n = rd.nextInt();
        int a[] = new int[n + 1];
        for(int i = 1; i <= n; i ++) a[i] = rd.nextInt();
        Arrays.sort(a);

        long dp[] = new long[n + 1];
        for(int i = 1; i <= n; i ++){
            if(a[i] > dp[i - 1] + 1){
                pw.println(dp[i - 1] + 1);
                return;
            }else{
                dp[i] = dp[i - 1] + a[i];
            }
            if(dp[i] >= n) break;
        }
        pw.println("Cool!");
    }
```

[E-折返跑_牛客周赛 Round 60 (nowcoder.com)](https://ac.nowcoder.com/acm/contest/90070/E)

> **组合数学** $C_{n -2}^{m - 1}$
>
> 其中有$m - 1$次需要推杆，需要在两杆之间$n-2$个位置中选取$m-1$个落脚点

[F-口吃_牛客周赛 Round 60 (nowcoder.com)](https://ac.nowcoder.com/acm/contest/90070/F)

> **期望dp 推公式**
>
> $f_i$：从第$i$个字开始讲完这句话的期望
>
> 这样转移：$f_i = P_if_{i+1}+Q_i$
>
> $f_1=\frac{a_1}{a_1+b_1}f_2+\frac{b_1}{a_1+b_1}f_1 + 1 \rightarrow f_1=f_2+\frac{a_1+b_1}{a_1}$    $P_1=1,Q_1=\frac{a_1+b_1}{a_1}$
>
> $f_2=\frac{a_2^2}{(a_2+b_2)^2}f_3+\frac{2a_2b_2}{(a_2+b_2)^2}f_2+\frac{a_2^2}{(a_2+b_2)^2}f_3+1\rightarrow f_2=\frac{a_2^2}{a_2^2+b_2^2-b_2^2P_1}f_3+\frac{b_2^2Q_1+(a_2+b_2)^2}{a_2^2+b_2^2-b_2^2P_1}$
>
> $P_2=\frac{a_2^2}{a_2^2+b_2^2-b_2^2P_1},Q_2=\frac{b_2^2Q_1+(a_2+b_2)^2}{a_2^2+b_2^2-b_2^2P_1}$可以推广为$P_i=\frac{a_i^2}{a_i^2+b_i^2-b_i^2P_{i-1}},Q_i=\frac{b_i^2Q_{i-1}+(a_i+b_i)^2}{a_i^2+b_i^2-b_i^2P_{i-1}}$
>
> 正推`P[] Q[]`，逆推`f[]`

```java
    static int mod = (int)1e9 + 7;
    public static void solve() throws IOException{     
        int n = rd.nextInt();
        long a[] = new long[n];
        long b[] = new long[n];
        for(int i = 1; i <= n - 1; i ++) a[i] = rd.nextInt();
        for(int i = 1; i <= n - 1; i ++) b[i] = rd.nextInt();
        long P[] = new long[n];
        long Q[] = new long[n];
        P[1] = 1; Q[1] = (b[1] * pow(a[1], mod - 2) + 1) % mod;
        for(int i = 2; i <= n - 1; i ++){
            P[i] = pow(a[i], 2) * pow( (pow(a[i], 2) + pow(b[i], 2) + mod - pow(b[i], 2) * P[i - 1] % mod) % mod , mod - 2) % mod;
            Q[i] = (pow(b[i], 2) * Q[i - 1] + pow(a[i] + b[i] , 2)) % mod * pow( (pow(a[i], 2) + pow(b[i], 2) + mod - pow(b[i], 2) * P[i - 1] % mod) % mod , mod - 2) % mod;
        }
        long f[] = new long[n + 1];
        f[n] = 1;
        for(int i = n - 1; i >= 1; i --){
            f[i] = (P[i] * f[i + 1] % mod+ Q[i]) % mod;
        }
        
        pw.println(f[1]);
    }   

    public static long pow(long a, long n){
        a %= mod;
        long ans = 1;
        while(n > 0){
            if(n % 2 == 1) ans = ans * a % mod;
            a = a * a % mod;
            n >>= 1;
        }
        return ans;
    }
```

