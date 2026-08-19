# dijkstra

> **非负权图**单源最短路算法。



[牛客 226498](https://ac.nowcoder.com/acm/problem/226498)

距离不大，用数组装点和边

```java
import java.io.*;
import java.util.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static int n, m, d[], N = 5050, inf = (int)1e9;
    static boolean vis[];
    static Vector<int[]> adj[];
    static Queue<int[]> que = new PriorityQueue<>((o1, o2) -> Integer.compare(o1[1], o2[1]));
    public static void main(String[] args) throws IOException {
        n = sc.nextInt();        
        m = sc.nextInt();
        d = new int[N];
        vis = new boolean[N];
        adj = new Vector[N];
        Arrays.setAll(adj, i -> new Vector<>());
        while(m --> 0){
            int u = sc.nextInt();
            int v = sc.nextInt();
            int c = sc.nextInt();
            adj[u].add(new int[]{v, c});
            adj[v].add(new int[]{u, c});
        }
        Arrays.fill(d, inf);
        d[1] = 0;
        que.add(new int[]{1, d[1]});
        while(!que.isEmpty()){
            int u[] = que.poll();
            if(vis[u[0]]) continue;
            vis[u[0]] = true;
            for(int v[] : adj[u[0]]){
                if(d[v[0]] > d[u[0]] + v[1]){
                    d[v[0]] = d[u[0]] + v[1];
                    que.add(new int[]{v[0], d[v[0]]});
                }
            }
        }
        pw.println(d[n] == inf ? -1 : d[n]);
        pw.flush();pw.close();
    }
}
```



[洛谷 AT_abc362_d](https://www.luogu.com.cn/problem/AT_abc362_d)

距离较大，需要用类表示边

```java
import java.io.*;
import java.util.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static int n, m, a[];
    static long d[], INF = (long)1e18;
    static boolean vis[];
    static Vector<E> adj[];
    static Queue<E> que = new PriorityQueue<>((e1, e2) -> Long.compare(e1.w, e2.w));
    static class E{
        int v; long w;
        public E(int v, long w){this.v = v; this.w = w;}
    }
    public static void main(String[] args) throws IOException {
        n = sc.nextInt();
        m = sc.nextInt();
        a = new int[n + 1];
        for(int i = 1; i <= n; i ++) a[i] = sc.nextInt();
        d = new long[n + 1];
        vis = new boolean[n + 1];
        adj = new Vector[n + 1];
        Arrays.setAll(adj, i -> new Vector<>());
        while(m --> 0){
            int u = sc.nextInt();
            int v = sc.nextInt();
            int c = sc.nextInt();
            adj[u].add(new E(v, c));
            adj[v].add(new E(u, c));
        }
        //--
        Arrays.fill(d, INF);
        d[1] = a[1];
        que.add(new E(1, d[1]));
        while(!que.isEmpty()){
            E pos = que.poll();
            int u = pos.v;
            long step = pos.w;
            if(vis[u]) continue;
            vis[u] = true;
            for(E ne : adj[u]){
                if(d[ne.v] > d[u] + ne.w + a[ne.v]){
                    d[ne.v] = d[u] + ne.w + a[ne.v];
                    que.add(new E(ne.v, d[ne.v]));
                }
            }
        }
        for(int i = 2; i <= n; i ++) pw.print(d[i] + " ");
        pw.flush();pw.close();
    }
}
```
