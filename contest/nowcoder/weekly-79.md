# ✅牛客周赛 Round 79

[D-小红的“质数”寻找_牛客周赛 Round 79](https://ac.nowcoder.com/acm/contest/100902/D) 

> 思维
>
> 考虑一下在$[x, 2\times x]$中位数和最小是多少，假设$x$的第一位为$t$，那么位数和为$t+1$的数肯定在范围中（第一位为$t + 1$后面全是0），这样我们就能根据$x$的第一位来构造这样一个数了。第一位为$1\sim9$的情况都算一下，发现他们分别对应$2,3,5,7,7,7,11,11,11$，在后面补0补到它在对应范围内。

```java
    static int[] ans = new int[]{0, 2, 3, 5, 7, 7, 7, 11, 11, 11};
    public static void solve() throws IOException {
        String s = rd.next();
        int t = s.charAt(0) - '0';
        pw.print(ans[t]);
        for(int i = 1; i < s.length(); i ++) pw.print("0");
        pw.print("\n");
    }
```

[E-小红的好排列_牛客周赛 Round 79](https://ac.nowcoder.com/acm/contest/100902/E)

> **排列、组合**
>
> 要的使得$a_i\times i$是3的倍数，必须要求他们其中至少一个是3的倍数。3的倍数的$a_i$和$i$都有$k=\lfloor \frac{n}{3}\rfloor$个，我们将他们一些重叠着放，一些错位着放，那么就能凑出答案。显然，最多可以凑出$2k$个3的倍数，如果$2k<\frac{n}{2}$，那么就只有0个答案；若$2k\ge \frac{n}{2}$，那么需要重叠着放$m=2k-\frac{n}{2}$个即可。从$k$个数中选取$m$个数放入$k$个位置中，即$C_k^mA_k^m$。剩下的3的倍数就不能放入3倍数位置了，他们必须放入$n-k$个非3倍数位置中，即$A_{n-k}^{k-m}$。最后再放剩下的$n-k$个数，即$A_{n-k}^{n-k}$。再把这几项乘起来即为答案。

```java
    // ...省略板子
	public static void solve() throws IOException {
        init();
        int n = rd.nextInt();
        int k = n / 3; // 排列中有几个3的倍数
        if (2 * k < n / 2) { // 不够
            pw.println(0);
            return;
        }
        int m = 2 * k - n / 2; // 需要m个3的倍数摆放在3的倍数位置
        pw.println(C(k, m) * A(k, m) % mod * A(n - k, k - m) % mod * A(n - k, n - k) % mod);
    }
```

[F-小红的小球染色期望_牛客周赛 Round 79](https://ac.nowcoder.com/acm/contest/100902/F)

> **期望dp** 
>
> 定义$dp[i]$：$i$个小球一排操作的期望
>
> 初始化：$dp[0]=0, dp[1]=0,dp[2]=1$
>
> 递推公式：对于一排没有操作过的小球，考虑第一次操作，第一次操作可以有$i-1$个位置，操作每个位置的概率为$\frac{1}{i-1}$，一次操作$j$把小球分成了长度为$j$和$i-j-2$左右两段，这一次的操作的期望为$\frac{1}{i-1}\times (dp[j]+dp[i-j-2]+1)$，我们将每一次的操作的期望加起来就可以推出长度$i$小球的操作期望：$\sum_{j=0}^{i-2}(\frac{1}{i-1}\times (dp[j]+dp[i-j-2]+1))$，可以化简：$\frac{2}{i-1}\times\sum_{j=0}^{i-2}dp[j]+1$。其中求和部分用前缀和维护。

```java
    static int mod = (int)1e9 + 7;
    public static long qpow(long a, long n) {
        long ans = 1;
        while (n > 0) {
            if (n % 2 == 1)
                ans = ans * a % mod;
            a = a * a % mod;
            n >>>= 1;
        }
        return ans;
    }
    public static void solve() throws IOException {
        int n = rd.nextInt();
        int maxn = (int)1e6 + 10;
        long dp[] = new long[maxn + 1];
        long pre[] = new long[maxn + 1];
        dp[0] = 0; dp[1] = 0; dp[2] = 1;
        pre[2] = 1;
        for(int i = 3; i <= n; i ++){
            dp[i] = 2 * pre[i - 2] * qpow(i - 1, mod - 2) % mod + 1;
            pre[i] = (pre[i - 1] + dp[i]) % mod;
        }       
        pw.println(dp[n]); 
    }
```

