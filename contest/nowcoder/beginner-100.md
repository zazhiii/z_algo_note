# 牛客小白月赛100 (exc: F)

[D-ACM中的AC题_牛客小白月赛100 (nowcoder.com)](https://ac.nowcoder.com/acm/contest/88878/D)

> BFS
>
> 每个状态存**和起点对称的两个点坐标**和**步数**，当搜索到一个点出去之后，当前步数再加上另一个点到最近传送门的距离（这个距离通过预处理后快速得到），搜索所有情况取最小值。
>
> $O(n\times m)$

```java
import java.io.*;
import java.util.*;
public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(System.out);
    static int[] dx1 = {1, -1, 0, 0}, dy1 = {0, 0, 1, -1};
    static int[] dx2 = {-1, 1, 0, 0}, dy2 = {0, 0, -1, 1};
    static char a[][];
    static int inf = (int)1e9;
    public static void solve(){
        int n = sc.nextInt();
        int m = sc.nextInt();
        int x0 = sc.nextInt();
        int y0 = sc.nextInt();
        x0 --;
        y0 --;
        a = new char[n][m];
        for(int i = 0; i < n; i ++) a[i] = sc.next().toCharArray();
        Queue<int[]> que = new ArrayDeque<>();
        boolean vis[][] = new boolean[n][m];
        int dist[][] = new int[n][m];
        for(int i = 0; i < n; i ++){
            for(int j = 0; j < m; j ++){
                dist[i][j] = inf;
                if(a[i][j] == '@'){
                    que.add(new int[]{i, j, 0});
                    dist[i][j] = 0;
                    vis[i][j] = true;
                }
            }
        }
        while(!que.isEmpty()){
            int pos[] = que.poll();
            int x = pos[0]; int y = pos[1]; int k = pos[2];
            for(int i = 0; i < 4; i ++){
                int nx = x + dx1[i]; int ny = y + dy1[i];
                if(nx >= 0 && nx < n && ny >= 0 && ny < m && !vis[nx][ny] && a[nx][ny] != '#'){
                    que.add(new int[]{nx, ny, k + 1});
                    dist[nx][ny] = k + 1;
                    vis[nx][ny] = true;
                }
            }
        }
        int ans = inf;
        que = new ArrayDeque<>();
        vis = new boolean[n][m];
        que.add(new int[]{x0, y0, x0, y0, 0});
        vis[x0][y0] = true;
        while(!que.isEmpty()){
            int pos[] = que.poll();
            int x1 = pos[0]; int y1 = pos[1]; int x2 = pos[2]; int y2 = pos[3]; int k = pos[4];
            if(a[x1][y1] == '@'){
                ans = Math.min(ans, k + dist[x2][y2]);
            }
            if(a[x2][y2] == '@'){
                ans = Math.min(ans, k + dist[x1][y1]);
            }
            for(int i = 0; i < 4; i ++){
                int nx1 = x1 + dx1[i]; int ny1 = y1 + dy1[i];
                int nx2 = x2 + dx2[i]; int ny2 = y2 + dy2[i];
                if(nx1 >= 0 && nx1 < n && ny1 >= 0 && ny1 < m && !vis[nx1][ny1] && a[nx1][ny1] != '#' &&
                nx2 >= 0 && nx2 < n && ny2 >= 0 && ny2 < m && !vis[nx2][ny2] && a[nx2][ny2] != '#'){
                    que.add(new int[]{nx1, ny1, nx2, ny2, k + 1});
                    vis[nx1][ny1] = true;
                    vis[nx2][ny2] = true;
                }
            }
        }
        pw.println(ans == inf ? -1 : ans);
    }
    public static void main(String args[]) throws IOException {
        solve();
        pw.flush();
    }   
}
```

[E-ACM中的CM题_牛客小白月赛100 (nowcoder.com)](https://ac.nowcoder.com/acm/contest/88878/E)

> 枚举+二分
>
> 枚举排雷能力，将地雷位置排序，从第一个开始往后跳，看需要跳多少次，下一个跳到什么位置通过二分得到
>
> $O(n\log n)$

```java
    public static void solve(){
        int n = sc.nextInt();
        int maxn = 200010;
        int a[] = new int[n + 1];
        for(int i = 1; i <= n; i ++) a[i] = sc.nextInt();
        Arrays.sort(a);
        int ans = (int)1e9;
        for(int i = 1; i <= maxn; i ++){
            int cnt = 1, p = 1;
            while(p < n){
                int l = p, r = n, idx = n + 1;
                while(l <= r){
                    int m = (l + r) >>> 1;
                    if(a[m] >= a[p] + i){idx = m; r = m - 1;}
                    else l = m + 1;
                }
                p = idx;
                if(p <= n) cnt ++;
            }
            ans = Math.min(ans, cnt + i - 1);
        }
        pw.println(ans);
    }
```

