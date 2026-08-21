# [牛客周赛 Round 93](https://ac.nowcoder.com/acm/contest/109904)（exc：F）

[D-死_牛客周赛 Round 93](https://ac.nowcoder.com/acm/contest/109904/D)

> 贪心
>
> 将$2\sim n$位置中的前$k$大加到第一个数上，**相同的数优先取靠后的**

```java
    static public void solve() throws IOException {
        int n = rd.nextInt();
        int k = rd.nextInt();
        int[] a = new int[n];
        // 排序有讲究
        PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> o2[1] == o1[1] ? o2[0] - o1[0] : o2[1] - o1[1]);
        for (int i = 0; i < n; i++) {
            a[i] = rd.nextInt();
            if(i > 0) pq.add(new int[]{i, a[i]});
        }
        long sum = 0;
        boolean[] f = new boolean[n];
        while(k --> 0){
            int[] t = pq.poll();
            sum += t[1];
            f[t[0]] = true;
        }
        pw.print((sum + a[0]) + " ");
        for(int i = 1; i < n; i ++){
            if(!f[i]){
                pw.print(a[i] + " ");
            }
        }
        pw.println();
    }
```



[E-不_牛客周赛 Round 93](https://ac.nowcoder.com/acm/contest/109904/E)

> 组合数学
>
> 两种序列满足条件
>
> 1. 从0开始连续的序列 
> 2. 全部相同的序列
>
> $C_n^1+C_n^2+...C_n^n=2^n-1$

```java
    static int mod = (int)1e9 + 7;
    static public void solve() throws IOException {
        int n = rd.nextInt();
        int[] a = new int[n];
        Map<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < n; i ++){
            a[i] = rd.nextInt();
            map.put(a[i], map.getOrDefault(a[i], 0) + 1);
        }
        long ans = 0;
        for(Integer v: map.values()){
            ans = (ans + qpow(2, v) - 1) % mod;
        }
        long m = qpow(2, map.getOrDefault(0, 0)) - 1;
        for(int i = 1; i < 1e6 + 1; i ++){
            if(!map.containsKey(i)) break;
            m = m * (qpow(2, map.get(i)) - 1) % mod;
            ans = (ans + m) % mod;
        }
        pw.println(ans);
    }

    public static long qpow(long a, long n){
        long res = 1;
        while(n > 0){
            if(n % 2 == 1) res = res * a % mod;
            a = a * a % mod;
            n >>= 1;
        }
        return res;
    }
```

