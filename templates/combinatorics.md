# 组合数学模板

## 模板

$C_a^b$当$a$和$b$较小时（$0\le b\le a\le2000$），用`c[a][b]`存储$C_a^b$的值，利用递推式$C^m_n=C^m_{n−1}+C^{m−1}_{n−1}$计算出所有组合数的值。

```java
static int c[][], N = 2020, mod = (int)1e9 + 7;

public static void init(){
    c = new int[N][N];
    for(int i = 0; i < N; i ++){
        for(int j = 0; j <= i; j ++){
            if(j == 0) c[i][j] = 1; //c[i][0] = 1
             else c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % mod;
        }
    }
}
/* c[a][b] */
```



当$a$和$b$较大（$1\le b\le a\le10^5$），预处理阶乘和阶乘的逆元，利用组合数公式$\frac{n!}{m!(n-m)!}$计算每一个组合数。

```java
static int N = (int)1e6 + 10, mod = (int)1e9 + 7;
static long f[] = new long[N], invf[] = new long[N];

// 预处理阶乘和阶乘的逆元
public static void init(){
    f[0] = invf[0] = 1;
    for(int i = 1; i < N; i ++){
        f[i] = f[i - 1] * i % mod;
        invf[i] = invf[i - 1] * qpow(i, mod - 2) % mod;
    }
}

//快速幂，用以计算逆元
public static long qpow(long a, long n){
    long ans = 1;
    while(n > 0){
        if(n % 2 == 1) ans = ans * a % mod;
        a = a * a % mod;
        n >>>= 1;
    }
    return ans;
}

// 用排列数公式计算排列 
public static long A(int a, int b){
    return f[a] * invf[a - b] % mod;
}

// 用组合数公式计算组合
public static long C(int a, int b){
    if(b > a) return 0;
    return f[a] * invf[b] % mod * invf[a - b] % mod;
}
```



## 题目

[Problem - 1999F - Codeforces](https://codeforces.com/problemset/problem/1999/F)

[E-小红的好排列_牛客周赛 Round 79](https://ac.nowcoder.com/acm/contest/100902/E)