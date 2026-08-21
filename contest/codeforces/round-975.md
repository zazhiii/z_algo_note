# [Round 975 (Div. 2)](https://codeforces.com/contest/2019) (exc: D E F)

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

