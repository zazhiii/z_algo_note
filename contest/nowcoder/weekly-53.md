# [牛客周赛 Round 53](https://ac.nowcoder.com/acm/contest/86387)

[D-小红组比赛_“葡萄城杯”牛客周赛 Round 53 (nowcoder.com)](https://ac.nowcoder.com/acm/contest/86387/D)

有$n$行数，每行$m$个，在其中每行选一个数使得与$target$最接近，输出最小相差多少。

$1\le n \le100,1\le m\le20\\1\le a_{i,j}\le50\\1\le target\le5000$

> dp

> $dp[i][x]$：选$i$个数是否能获得值$x$
>
> 转移：$dp[i][x] |=dp[i-1][x-a[i][j]]$，能否获得$x$和上一行能否获得$x-a[i][j]$有关
>
> 注意：转移时用 `|=` 不能直接用 `=` ，因为同一行选不同数时会可能会转移出相同$x$值；如果直接赋值，若靠前的可以转移出该$x$，靠后的不能转移出$x$，那么之前的结果就会被不能转移出覆盖，导致错误。所以用`|=`保证已经转移出的结果保留。
>
> 转移出第$n$行能够获得的数据之后，遍历一遍记录与$target$最小的差值。

> $O(n\times m\times target)$

```java
import java.io.*;
import java.util.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static int n, m, a[][], t;
    static boolean dp[][];
    public static void main(String[] args) throws IOException {
        n = sc.nextInt();
        m = sc.nextInt();
        a = new int[n + 1][m];
        dp = new boolean[n + 1][100010];
        for(int i = 1; i <= n; i ++)
            for(int j = 0; j < m; j ++)
                a[i][j] = sc.nextInt();
        t = sc.nextInt();
        dp[0][0] = true;
        for(int i = 1; i <= n; i ++)
            for(int j = 0; j < m; j ++)
                for(int x = a[i][j]; x <= 5000; x ++)
                    dp[i][x] |= dp[i - 1][x - a[i][j]];
        int ans = (int)1e9;
        for(int x = 0; x < dp[n].length; x ++){
            if(dp[n][x]) ans = Math.min(ans, Math.abs(t - x));
        }
        pw.println(ans);
        pw.flush();pw.close();
    }
}
```

[E-折半丢弃_“葡萄城杯”牛客周赛 Round 53 (nowcoder.com)](https://ac.nowcoder.com/acm/contest/86387/E)

> 二分答案

> 小于等于最大mex的都可以满足，而大于最大mex的不能满足，所以可以二分mex再验证该mex是否满足。
>
> 验证二分的mex是否满足：对于所有大于mex的值，将其不断除以2，直到小于该mex且没有出现过的值时停止。如果一直除到0也没有遇见还没出现过的数，也停止。最后判断mex之前是否有mex个数即可。

> $O(n\log^2 n)$

```java
import java.io.*;
import java.util.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static int n, a[];
    public static boolean check(int m){
        Set<Integer> set = new HashSet<>();
        boolean vis[] = new boolean[m];
        for(int i = 0; i < n; i ++){
            int t = a[i];
            while(t >= m || (t > 0 && set.contains(t))) t /= 2;
            set.add(t);
        }
        return set.size() == m;
    }
    public static void solve(){
        n = sc.nextInt();
        a = new int[n];
        for(int i = 0; i < n; i ++) a[i] = sc.nextInt();
        int l = 1, r = n + 1, ans = 0;
        while(l <= r){
            int m = (l + r) >>> 1;
            if(check(m)){
                ans = m;
                l = m + 1;
            }else{
                r = m - 1;
            }
        }
        pw.println(ans);
    }
    public static void main(String[] args) throws IOException {
        int T = sc.nextInt();
        while(T --> 0) solve();
        pw.flush();pw.close();
    }
}
```

[F-小红走矩阵_“葡萄城杯”牛客周赛 Round 53 (nowcoder.com)](https://ac.nowcoder.com/acm/contest/86387/F)

​		$n×m$ 的矩阵由障碍和空地组成，初始时小红位于起点 $(1, 1)$ ，她想要前往终点 $(n,m)$。小红每一步可以往上下左右四个方向的空地移动一格。
​		小红在起点处可以进行最多一次操作：选择矩阵中的一处障碍替换为空地，但代价是小红必须选择失去向上下左右四个方向中一个移动的能力。
​		求小红从起点到达终点的最小步数，如果无法到达则输出 −1

> BFS

> 状态存储：$[x,y,step,ban,k]$表示坐标、步数、不能走的方向、还能穿过的障碍数。
>
> $vis$数组防止重复搜索：$[x,y,ban,k]$记录是否被搜索过。

> $O(n\times m \times 5\times 2)$

```java
import java.io.*;
import java.util.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static int n, m;
    static char[][] c;
    static boolean vis[][][][];
    static int dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};
    public static void main(String[] args) throws IOException {
        n = sc.nextInt();
        m = sc.nextInt();
        c = new char[n][];
        vis = new boolean[n][m][5][2];
        for(int i = 0; i < n; i ++){
            c[i] = sc.next().toCharArray();
        }
        int ans = -1;
        // x y step ban k
        Queue<int[]> que = new LinkedList<>();
        que.add(new int[]{0, 0, 0, 0, 1});
        que.add(new int[]{0, 0, 0, 1, 1});
        que.add(new int[]{0, 0, 0, 2, 1});
        que.add(new int[]{0, 0, 0, 3, 1});
        que.add(new int[]{0, 0, 0, 4, 0});
        while(!que.isEmpty()){
            int p[], x, y, step, ban, k;
            p = que.poll();
            x = p[0]; y = p[1]; step = p[2]; ban = p[3]; k = p[4];            
            if(x < 0 || x >= n || y < 0 || y >= m) continue;
            if(vis[x][y][ban][k]) continue;
            if(c[x][y] == 'X' && k == 0) continue;
            vis[x][y][ban][k] = true;
            if(x == n - 1 && y == m - 1){
                ans = step;
                break;
            }
            if(c[x][y] == 'X') k = 0;
            for(int i = 0; i < 4; i ++){
                if(i == ban) continue;
                que.add(new int[]{x + dx[i], y + dy[i], step + 1, ban, k});
            }

        }
        pw.println(ans);
        pw.flush();pw.close();
    }
}
```

