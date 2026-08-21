# 牛客周赛 Round 50

[D-小红的因式分解](https://ac.nowcoder.com/acm/contest/85687/D)

小红有三个整数 $a,b,c$，要将 $ax^2+bx+c$分解为 $(a_1x+b_1)(a_2x+b_2)$ 的形式，其中 $a_1,b_1,a_2,b_2$ 均为整数。如果可以分解，请按 $a_1,b_1,a_2,b_2$的顺序输出，若有多解输出任意一种，若无解，输出 "NO"。

> 数学、枚举

> 法一 ： 枚举
>
> 枚举所有相乘等于$a$的$a_1,a_2$数对，和相乘等于$b$的$b_1,b_2$数对。判断里面是否有$a_1\times b_2 + a_2 \times b_1=b$的情况。
>
> 法二：解方程
>
> 从方程的解出发。若delta小于0则无解，再用求根公式计算方程的解的分子分母是否为整数。若为整数求解出最简分数形式，再计算$a_1\times a_2 和a$的倍数差，再乘上倍数。
>
> **注意**：计算delta的时候会超`int`

```java
import java.io.*;
import java.util.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static int a, b, c;
    public static void solve(){
        a = sc.nextInt();
        b = sc.nextInt();
        c = sc.nextInt();
        // if(b * b - 4 * a * c < 0) pw.println("NO");
        // else{
            if(c==0) {
                pw.println(1 + " " + 0 + " " + a + " " + b);
                return;
            }
            Vector<int[]> p = new Vector<>();
            Vector<int[]> q = new Vector<>();
            for(int i = 1; i * i <= Math.abs(a); i ++){
                if(Math.abs(a) % i == 0){
                    p.add(new int[]{i, a / i});
                    p.add(new int[]{a / i, i});
                    p.add(new int[]{-i, -a / i});
                    p.add(new int[]{-a / i, -i});
                }
            }
            for(int i = 1; i * i <= Math.abs(c); i ++){
                if(Math.abs(c) % i == 0){
                    q.add(new int[]{i, c / i});
                    q.add(new int[]{c / i, i});
                    q.add(new int[]{-i, -c / i});
                    q.add(new int[]{-c / i, -i});
                }
            }
            for(int[] A : p){
                for(int[] B : q){
                    if(1l * A[0] * B[1] +  1l * A[1] * B[0] == b){
                        pw.println(A[0] + " " + B[0] + " " + A[1] + " " + B[1]);
                        return;
                    }
                }
            }            
            pw.println("NO");
        }
    // }
    public static void main(String[] args) throws IOException {
        int T = sc.nextInt();
        while(T --> 0) solve();
        pw.flush();pw.close();
    }
}
----------------------------------------------------------------------
import java.io.*;
import java.util.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static int a, b, c;
    public static void solve(){
        a = sc.nextInt();
        b = sc.nextInt();
        c = sc.nextInt();
        long d = 1l * b * b - 4l * a * c;
        if(d < 0){
            pw.println("NO");
            return;
        }
        long sq = (long)Math.sqrt(d);
        if(sq * sq != d){
            pw.println("NO");
            return;
        }
        long a1 = 2 * a;
        long b1 = b - sq;
        long a2 = 2 * a;
        long b2 = b + sq;
        long g1 = gcd(a1, b1);
        long g2 = gcd(a2, b2);
        a1 /= g1;
        b1 /= g1;
        a2 /= g2;
        b2 /= g2;
        long dd = a / a1 / a2;
        a1 *= dd;
        b1 *= dd;
        pw.println(a1 + " " + b1 + " " + a2 + " " + b2);
    }
    public static long gcd(long a, long b){
        return b == 0 ? a : gcd(b, a % b);
    }
    public static void main(String[] args) throws IOException {
        int T = sc.nextInt();
        while(T --> 0) solve();
        pw.flush();pw.close();
    }
}
```

[E-小红的树上移动](https://ac.nowcoder.com/acm/contest/85687/E)

小红有一棵 $n$ 个点的树，根节点为 1，有一个物块在根节点上，每次它会等概率随机移动到当前节点的其中一个子节点，而后等概率随机传送到一个同深度节点，若此时它位于叶子节点，则停止移动。
 求其移动到子节点的次数的期望值，答案对 $998244353$取模。

> 期望、概率，dfs，快速幂，逆元。

> 注意这句话“每次它会等概率随机移动到当前节点的其中一个子节点，而后等概率随机传送到一个同深度节点”
>
> 代表从一层移动下一层的每个点的概率相同。
>
> 用dfs统计每一层有多少节点和多少叶子节点。
>
> 对于**每一层的期望**为到达这一层的叶子节点的概率乘以这一层的深度（定义根节点深度为0），**到达这一层的的叶子节点的概率**为到上一层非叶子节点的概率乘以这一层叶子节点的占比。

```java
import java.io.*;
import java.util.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static int n, u, v, lay[], yz[], mod = 998244353;
    static Vector<Integer>[] adj;
    public static long qpow(long a,long n){
        a %= mod;
        long ans = 1;
        while(n > 0){
            if(n % 2 == 1) ans = ans * a % mod;
            a = a * a % mod;
            n >>>= 1;
        }
        return ans;
    }
    public static void main(String[] args) throws IOException {
        n = sc.nextInt();
        adj = new Vector[n + 1];
        lay = new int[n + 2];
        yz = new int[n + 2];
        Arrays.setAll(adj, i -> new Vector<>());        
        for(int i = 1; i < n; i ++){
            u = sc.nextInt();
            v = sc.nextInt();
            adj[u].add(v);
        }
        dfs(1, 1);
        long ans = 0, p = 1;
        for (int i = 1; i <= n; i++) {
            // pw.print(lay[i] + " " + yz[i] + "\n");
            ans = (ans + p * yz[i] % mod * qpow(lay[i], mod - 2) % mod * (i - 1)) % mod;
            p = p * (lay[i] - yz[i]) % mod * qpow(lay[i], mod - 2) % mod;
        }
        pw.println(ans);
        pw.flush();pw.close();
    }
    public static void dfs(int u, int c){
        lay[c] ++;
        if(adj[u].size() == 0) yz[c] ++;
        for(int v : adj[u]){
            dfs(v, c + 1);
        }
    }
}
```

