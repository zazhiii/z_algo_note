# 牛客周赛 Round 54（exc: E F）

[D-清楚姐姐跳格子_牛客周赛 Round 54 (nowcoder.com)](https://ac.nowcoder.com/acm/contest/87303/D)

清楚正在玩跳格子游戏。地上有 n 个格子，清楚一开始在 1 号格子，目标是 n 号格子。

第 $i$ 个格子上有一个数字 $a_i$ ，清楚在这个格子上可以往左右两边选一个方向，然后选择 $a_i$ 的一个正整数因子作为长度，进行一次跳跃，但是不可以跳出边界。
请问清楚最少跳多少步，就可以到达 $n$ 号格子。

> 最短路

> 对于每个数我们求解他的因数距离是哪些格子并不好操作，我们反过来枚举格子距离判断是否是他的因数。
>
> 法一：BFS，标记已经搜索过的地方，防止重复搜索。
>
> 法二：用朴素版的dijkstra。

> $O(???)$
>
> $O(n^2)$

```java
import java.io.*;
import java.util.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static int n, d[];
    static long a[];
    public static void solve(){
        n = sc.nextInt();
        a = new long[n + 1];
        d = new int[n + 1];
        for(int i = 1; i <= n; i ++) a[i] = sc.nextLong();
        Arrays.fill(d, -1);
        Queue<int[]> que = new LinkedList<>();
        que.add(new int[]{1, 0});
        d[1] = 0;
        while(!que.isEmpty()){
            int p[] = que.poll();
            int t = p[0];
            int step = p[1];
            if(t == n){
                pw.println(step);
                return;
            }
            for(int i = (int) Math.max(0, t - a[t]); i <= Math.min(n, t + a[t]); i ++){
                if(d[i] == -1 && a[t] % Math.abs(i - t) == 0){
                    d[i] = step + 1;
                    que.add(new int[]{i, step + 1});
                }
            }
        }
    }
    public static void main(String[] args) throws IOException {     
        solve();
        pw.flush();pw.close();
    }  
}
//--------------------------------------------------------------

import java.io.*;
import java.util.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static int n, d[];
    static long a[];
    static boolean st[];
    public static void solve(){
        n = sc.nextInt();
        a = new long[n + 1];
        d = new int[n + 1];
        st = new boolean[n + 1];
        for(int i = 1; i <= n; i ++) a[i] = sc.nextLong();
        Arrays.fill(d, (int)1e9);
        d[1] = 0;
        for(int i = 0; i < n; i ++){
            int t = -1;
            for(int j = 1; j <= n; j ++){
                if(!st[j] && (t == -1 || d[j] < d[t])) t = j;
            }
            st[t] = true;
            for(int j = (int) Math.max(0, t - a[t]); j <= Math.min(n, t + a[t]); j ++){
                if(!st[j] && a[t] % Math.abs(j - t) == 0) d[j] = Math.min(d[j], d[t] + 1);
            }
        }
        pw.println(d[n]);
    }
    public static void main(String[] args) throws IOException {     
        solve();
        pw.flush();pw.close();
    }
}
```

