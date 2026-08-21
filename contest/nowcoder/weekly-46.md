# ✅牛客周赛 Round 46

[C-爱音开灯](https://ac.nowcoder.com/acm/contest/84444/C)

有无穷个灯排成一排，编号为从 1 开始，初始时所有灯都是关闭的。改变第 i 个灯的开闭状态会同时改变所有编号为 iii 倍数的灯的开闭状态。
 Anon会从 1 到 n ，依次改变每一个灯的开闭状态，她想知道第 x 个灯最终的状态是什么？如果灯是关闭的，输出 "OFF" ，否则输出 "ON" 。

> 约数

> 枚举$x$的因数，判断有多少次在$n$以内即该点被操作多少次
>
> $O(\sqrt n)$

```java
import java.io.*;
import java.util.*;
public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static long n, x;
    public static void main(String[] args) throws Exception {
        int cnt = 0;
        n = sc.nextLong();
        x = sc.nextLong();
        for(int i = 1; i < x / i; i ++){
            if(x % i == 0){
                if(i <= n) cnt ++;
                if(x / i <= n) cnt ++;
            }
        }
        //这里不要算两次了
        if(x % Math.sqrt(x) == 0 && Math.sqrt(x) <= n) cnt ++;
        pw.println(cnt % 2 == 0 ? "OFF" : "ON");
        pw.flush();
        pw.close(); 
    }
}
```

[D-小灯做题](https://ac.nowcoder.com/acm/contest/84444/D)

> 分类讨论
>
> $mex(x,y) \in \{0, 1, 2\}$
>
> 先过滤0步的情况
>
> a	b	c
>
> **a	b	1|a	b	0**	
>
> a	0	1
>
> 2	0	1

```java
import java.io.*;
import java.util.*;
public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static int T, a, b, c, k;
    public static void main(String[] args) throws Exception {
        T = sc.nextInt();
        while(T --> 0){
            a = sc.nextInt();
            b = sc.nextInt();
            c = sc.nextInt();
            k = sc.nextInt();
            Set<Integer> s = new HashSet<>();
            s.add(a);s.add(b);s.add(c);
            int ans = -1;
            if(s.contains(k)) ans = 0;
            else if(k == 0) ans = 1;
            else if(k == 1){
                if(s.contains(0)) ans = 1;
                else ans = 2;
            }
            else if(k == 2){
                if(s.contains(0) && s.contains(1)){
                    ans = 1;
                }else if(!s.contains(0) && !s.contains(1)){
                    ans = 3;
                }else{
                    ans = 2;
                }
            }
            pw.println(ans);            
        }
        pw.flush();
        pw.close(); 
    }
}
 
```

[E-立希喂猫](https://ac.nowcoder.com/acm/contest/84444/E)

Taki买了 n 种猫粮，第 i 种猫粮的营养值为 $a_i$ 、数量为 $b_i$ 。
 猫猫的饭量是无穷的，每一天她可以吃任意数量的猫粮，但是同一种猫粮她一天只会吃一次。
 Taki想知道在 k 天内，猫猫可以获得的最大营养值之和是多少

> **前缀和、二分、贪心**

> 对于每一天把还剩有的猫粮全部吃一遍，对于第$k$天，数量小于等于$k$的将被全部吃完，大于$k$的将被吃$k$次。
>
> 将猫粮按数量排序，二分查找出分界点，用两个前缀和计算两部分营养即可。

```java
import java.io.*;
import java.util.*;
public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static int n;
    static long a[][], s1[], s2[], q, k;
    public static void main(String[] args) throws Exception {
        n = sc.nextInt();
        a = new long[n + 1][2];
        s1 = new long[n + 1];
        s2 = new long[n + 1];
        for(int i = 1; i <= n; i ++) a[i][0] = sc.nextInt();
        for(int i = 1; i <= n; i ++) a[i][1] = sc.nextInt();
        Arrays.sort(a, (o1, o2) -> (int)(o1[1] - o2[1]));
        for(int i = 1; i <= n; i ++){
            s1[i] = s1[i - 1] + a[i][0] * a[i][1];
            s2[i] = s2[i - 1] + a[i][0];
        }
        q = sc.nextInt();
        while(q --> 0){
            k = sc.nextInt();
            int l = 0, r = n, idx = l;
            while(l <= r){
                int m = (l + r) >> 1;
                if(a[m][1] <= k){
                    idx = m;
                    l = m + 1;
                }else{
                    r = m - 1;
                }
            }
            pw.println( s1[idx] + k * (s2[n] - s2[idx]) );
        }

        pw.flush();
        pw.close(); 
    }
}
```

[F-祥子拆团](https://ac.nowcoder.com/acm/contest/84444/F)             

有两个数字 $x,y$ ，有多少种方式可以将 $x$ 拆成 $y$ 个正整数的乘积。
 例如 $x=6,y=2$ 时，有$6 \times 1=6,3 \times 2=6,2 \times 3=6,1 \times 6=6$ 这 4 种方法。
 由于这个答案可能很大，因此你需要输出答案对 $10^9 + 7$ 取模后的结果。

> **组合数学、快速幂、逆元**

> 考虑将$x$分解质因数，对于**每种**质因数（设这种质因数有$d$个）相当于放入$y$个盒子中且允许有空盒子，对应**插板法的第二类问题**，答案为$C_{d+y-1}^{y-1}=C_{d+y-1}^{d}$，由于$d$的值很小不会超过30，所以用循环计算组合数。
>
> $\frac{(d+y-1)\times(d+y-2)\times...\times y}{d\times(d-1)\times...\times1}$，$d$从$d$到$1$。
>
> 每种质因数放入盒子相当于一个步骤，根据乘法原理，需要将每种质因数的答案相乘。

```java
import java.io.*;
import java.util.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static int N = 100010, T, a, b, mod = (int)1e9 + 7;
    public static void main(String[] args) throws Exception {
        T = sc.nextInt();
        while(T --> 0){
            a = sc.nextInt();
            b = sc.nextInt();
            long ans = 1;
            for(int i = 2; i <= a / i; i ++){
                if(a % i == 0){
                    int s = 0;
                    while(a % i == 0){
                        s ++;
                        a /= i;
                    }
                    //s个相同质因子放入b个盒子 => c(s + b - 1, s)
                    for(int k = s; k >= 1; k --){
                        ans = ans * (b - 1 + k) % mod;
                        ans = ans * qpow(k, mod - 2) % mod;
                    }
                }
            }
            if(a > 1)  ans = ans * b % mod;
            pw.println(ans);
        }
        pw.flush();
        pw.close(); 
    }
    private static long qpow(long a, long n) {
        a %= mod;
        long ans = 1;
        while(n > 0){
            if((n & 1) == 1) ans = ans * a % mod;
            a = a * a % mod;
            n >>>= 1;
        }
        return ans;
    }
}
```

