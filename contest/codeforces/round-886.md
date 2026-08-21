# [Round 886 (Div. 4)](https://codeforces.com/contest/1850) (exc: H)

[E. Cardboard for Pictures](https://codeforces.com/contest/1850/problem/E) 二分答案

[F. We Were Both Children](https://codeforces.com/contest/1850/problem/F)

>    枚举
>
>    枚举每一种青蛙跳跃的地方，用`cnt[n + 1]`计数。注意：步数一样的青蛙跳的地方都一样，不用重复枚举，用map 记录每一种步长的青蛙有多少个，枚举一次就行了。

```java
    static public void solve(int T) throws IOException{
        int n = rd.nextInt();
        Map<Integer,Integer> map = new HashMap<>();
        for(int i = 0; i < n; i ++){
            int x = rd.nextInt();
            map.put(x, map.getOrDefault(x, 0) + 1);
        }
        int cnt[] = new int[n + 1];
        for(int len : map.keySet()){
            int k = map.get(len);
            for(int j = len; j <= n; j += len) cnt[j] += k;
        }
        int ans = 0;
        for(int i = 1; i <= n; i ++) ans = Math.max(ans, cnt[i]);
        pw.println(ans);
    }
```

[G. The Morning Star](https://codeforces.com/contest/1850/problem/G)

>    在一条`—｜\ /`线上的两个点算一个答案。用四个 map 记录四种直线中的每一条直线上有多少个点。对于`——｜`线，用单个坐标即可区分；对于`\ /`，前者一条线上的$x+y=c$，后者$x-y=c$，用$c$即可代表一条直线。遍历一遍坐标，累加通过该点的四条直线上的其他点的数量即答案。

```java
    static public void solve(int T) throws IOException{
        int n = rd.nextInt();
        int x[] = new int[n];
        int y[] = new int[n];
        Map<Integer, Integer> col = new HashMap<>();
        Map<Integer, Integer> row = new HashMap<>();
        Map<Integer, Integer> R = new HashMap<>();
        Map<Integer, Integer> L = new HashMap<>();
        for(int i = 0; i < n; i ++){
            x[i] = rd.nextInt();
            y[i] = rd.nextInt();
            row.put(x[i], row.getOrDefault(x[i], 0) + 1);
            col.put(y[i], col.getOrDefault(y[i], 0) + 1);
            R.put(x[i] + y[i], R.getOrDefault(x[i] + y[i], 0) + 1);
            L.put(x[i] - y[i], L.getOrDefault(x[i] - y[i], 0) + 1);
        }
        long ans = 0;
        for(int i = 0; i < n; i ++){
            ans += row.get(x[i]) + col.get(y[i]) + R.get(x[i] + y[i]) + L.get((x[i] - y[i])) - 4;
        }
        pw.println(ans);
    }
```

