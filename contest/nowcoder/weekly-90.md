# ✅[牛客周赛 Round 90](https://ac.nowcoder.com/acm/contest/107500)



[C Tk的构造数组](https://ac.nowcoder.com/acm/contest/107500/C)

> 贪心、排序

```java
    static public void solve() throws IOException {
        int n = rd.nextInt();
        long[][] a = new long[n][2];
        for(int i = 0; i < n; i ++) {
            a[i][0] = 1L * rd.nextInt() * (i + 1);
            a[i][1] = i;
        }
        Arrays.sort(a, (o1, o2) -> o1[0] >= o2[0] ? 1 : -1);
        int[] b = new int[n];
        for(int i = 0; i < n; i ++) b[i] = rd.nextInt();
        Arrays.sort(b);
        int[] ans = new int[n];
        for(int i = 0; i < n; i ++){
            ans[(int)a[i][1]] = b[i];
        }
        for(int x : ans) pw.print(x + " ");
    }
```



[D 真爱粉Tk（三）](https://ac.nowcoder.com/acm/contest/107500/D)

> 二分答案
>
> 相关题目：[洛谷 P1182](https://www.luogu.com.cn/problem/P1182)

```java
    static public void solve() throws IOException {
        int n = rd.nextInt();
        int k = rd.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = rd.nextInt();
        long l = 0, r = (long) 1e18;
        while (l <= r) {
            long m = (l + r) >> 1; 
            if (check(a, m, k)) r = m - 1;
            else l = m + 1;
        }
        pw.println(l);
    }
    private static boolean check(int[] a, long m, int k) {
        long sum25 = 0, sum2 = 0, K = 0;
        for (int x : a) {
            long cnt25 = 0, cnt2 = 0, cnt5 = 0;
            for (char ch : String.valueOf(x).toCharArray()) {
                if(ch == '5'){ 
                    cnt25 += cnt2;
                    cnt5 ++;
                }else if(ch == '2'){
                    cnt2 ++;
                }
            }
            if(cnt25 > m) return false;
            sum25 += cnt25 + cnt5 * sum2; 
            sum2 += cnt2;
            if(sum25 > m){
                sum25 = cnt25;
                sum2 = cnt2;
                K ++;
            }
        }
        K ++;
        return K <= k;
    }
```

[E-Tk的染色树_牛客周赛 Round 90](https://ac.nowcoder.com/acm/contest/107500/E)

> 贪心
>
> 全部选成对的叶子节点，若叶子节点数是偶数则全部配对即可，若为奇数最后剩的叶子节点在配对一个权值最小的节点

```java
    static public void solve() throws IOException {
        int n = rd.nextInt();
        int[] w = new int[n + 1];
        for(int i = 1; i <= n; i ++) w[i] = rd.nextInt();
        List<Integer>[] adj = new List[n + 1];
        Arrays.setAll(adj, i -> new ArrayList<>());
        for(int i = 1; i < n; i ++){
            int u = rd.nextInt();
            int v = rd.nextInt();
            adj[u].add(v);
            adj[v].add(u);
        }
        long cnt = 0, min = INF, sum = 0;
        for(int i = 1; i <= n; i ++){
            if(adj[i].size() <= 1) {
                cnt ++;
                sum += w[i];
            }
            min = Math.min(min, w[i]);
        }
        pw.println(cnt % 2 == 0 ? sum : sum + min);
    }
```

[F-Tk的排列间异或_牛客周赛 Round 90](https://ac.nowcoder.com/acm/contest/107500/F)

> 位运算、贪心
>
> 从n到1，从高位贪心地去匹配

```java
    static public void solve() throws IOException {
        int n = rd.nextInt();
        int[] a = new int[n + 1];
        for(int i = 1; i <= n; i ++) a[i] = rd.nextInt();
        boolean[] vis = new boolean[n + 1];
        int[] ans = new int[n + 1];
        for(int i = n; i >= 1; i --){
            if(vis[i]) continue;
            int x = 0;
            for(int j = 20; j >= 0; j --){
                if(((i >> j) & 1) == 0) {
                    if((x | (1 << j)) < i){
                        x |= 1 << j;
                    }
                }
            }
            vis[x] = true;
            ans[i] = x;
            ans[x] = i;
        }
        for(int i = 1; i <= n; i ++) pw.print(ans[a[i]] + " ");
    }
```

