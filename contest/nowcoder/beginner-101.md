# 牛客小白月赛101  (exc: F)

[D-tb的平方问题_牛客小白月赛101 (nowcoder.com)](https://ac.nowcoder.com/acm/contest/90072/D)

给一个数组 A 。进行q次询问，每次询问给x ， 给出包含x位置且区间和为完全平方数的连续子数组个数。

$1\le n\le10^3,1\le q\le3\times10^5$

> 前缀和 | 二分 | 差分
>
> 预处理求出区间和为完全平方数的区间。枚举区间实现这一步。
>
> 两种方法求得答案
>
> 1. 求出$[1,x]$有$a$个左端点和$[1,x-1]$有$b$个右端点，包含$x$的区间数为$a-b$。可以用前缀和或者二分实现。
> 2. 用差分预处理每个点有几个区间覆盖
>
> $O(n^2)$

```java
   // 方法1
	public static void solve() throws IOException{     
        int n = rd.nextInt();
        int q = rd.nextInt();
        long pre[] = new long [n + 1];
        for(int i = 1; i <= n; i ++){
            pre[i] = rd.nextLong();
            pre[i] += pre[i - 1];
        }
        long R[] = new long[n + 1];
        long L[] = new long[n + 1];
        for(int i = 1; i <= n; i ++){
            for(int j = i; j <= n; j ++){
                long x = pre[j] - pre[i - 1];
                long t = (long)Math.sqrt(x);
                if(t * t == x) {
                    L[i] ++; 
                    R[j] ++;
                }
            }
            R[i] += R[i - 1];
            L[i] += L[i - 1];
        }

        while(q --> 0){
            int x = rd.nextInt();
            pw.println(L[x] - R[x - 1]);
        }
 // ===============================================================
        // 方法2
            public static void solve() throws IOException{
        int n = rd.nextInt();
        int q = rd.nextInt();
        long pre[] = new long[n + 1];
        for(int i = 1; i <= n; i ++) {
            pre[i] = rd.nextLong();
            pre[i] += pre[i - 1];
        }
        long b[] = new long[n + 2];
        for(int i = 1; i <= n; i ++){
            for(int j = i; j <= n; j ++){
                long x = pre[j] - pre[i - 1];
                long t = (long)Math.sqrt(x);
                if(t * t == x){
                    b[i] ++;
                    b[j + 1] --;
                }
            }
            b[i] += b[i - 1];
        }
        while(q --> 0){
            int x = rd.nextInt();
            pw.println(b[x]);
        }
    }
```



[E-tb的数数问题_牛客小白月赛101 (nowcoder.com)](https://ac.nowcoder.com/acm/contest/90072/E)

给定一个集合，若一个数的所有约数都在该集合中那么这个数为好数，求好数个数。$1\le n\le10^6$

> 类似埃式筛的思路，若一个数没有在这个集合中，那么他的倍数肯定不在这个集合中，将每一个不在集合中的数及其倍数全部筛掉即可，最后计数没有被筛掉的个数即好数个数。
>
> $O(n\log n)$

```java
    static int N = (int)1e6;
    public static void solve() throws IOException{     
        int n = rd.nextInt();
        boolean a[] = new boolean[N + 1];
        for(int i = 0; i < n; i ++) {
            int x = rd.nextInt();
            a[x] = true;
        }

        boolean f[] = new boolean[N + 1];
        for(int i = 1; i <= N; i ++){
            if(!a[i]){
                for(int j = i; j <= N; j += i) f[j] = true;
            }
        }
        int ans = 0;
        for(int i = 1; i <= N; i ++) if(!f[i]) ans ++;
        pw.println(ans);
    }
```

