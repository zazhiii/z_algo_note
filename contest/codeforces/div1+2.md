# [Pinely Round 4 (Div. 1 + 2)](https://codeforces.com/contest/1991)

[Problem - B - Codeforces](https://codeforces.com/contest/1991/problem/B)

给你一个由 $n - 1$ 个整数组成的数组 $b$ 。

构造长度为$n$的数组$a$使得$b_i=a_i\&a_{i+1}$，不存在则输出$-1$

> 构造

> 由$b_i=a_i\&a_{i+1}、b_{i+1}=a_{i+1}\&a_{i+2}$，当$b_i$中为$1$的位$a_i\ a_{i+1}$中必为$1$，同理对于$b_{i+1}$中为$1$的位$a_{i+1}$中也应为$1$，所以$a_{i+1}=b_i|b_{i+1}$ ，这样可以计算出$a_2\sim a_{n-1}$，令$a_1=b_1,a_n=b_{n-1}$。再去遍历一遍$a$数组判断是否合法即可。

> $O(n)$

```java
import java.io.*;
import java.util.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    public static void solve(){
        int a[], b[];
        int n = sc.nextInt();
        a = new int[n];
        b = new int[n - 1];
        for(int i = 0; i < n - 1; i ++) b[i] = sc.nextInt();
        a[0] = b[0];
        a[n - 1] = b[n - 2];
        for(int i = 1; i <= n - 2; i ++) a[i] = b[i - 1] | b[i];
        for(int i = 0; i <= n - 2; i ++){
            if((a[i] & a[i + 1]) != b[i]){
                pw.println(-1);
                return;
            }
        }
        for(int i = 0; i < n; i ++) pw.print(a[i] + " ");
        pw.print("\n");
    }
    public static void main(String[] args) throws IOException {
        int T = sc.nextInt();
        while(T --> 0) solve();
        pw.flush();pw.close();
    }
}
```

[Problem - C - Codeforces](https://codeforces.com/contest/1991/problem/C)

You are given an array $a$ of $n$ integers.

In one operation, you will perform the following two-step move:

1.  Choose an integer $x$ ($0 \le x \le 10^{9}$).
2.  Replace each $a_i$ with $|a_i - x|$.

For example, by choosing $x = 8$, the array $[5, 7, 10]$ will be changed into $[|5-8|, |7-8|, |10-8|] = [3,1,2]$.

Construct a sequence of operations to make all elements of $a$ equal to $0$ in at most $40$ operations or determine that it is impossible. You do **not** need to minimize the number of operations.

> 构造，贪心

> 首先，如果序列中同时存在奇数和偶数就不可能操作成功，因为操作不可能把他们变为同奇偶的数。
>
> 考虑每次选择$x=[max(a_i)-min(a_i)]/2$因为这样能使极差减小得最快，直到$max(a_i)=min(a_i)$即可停止操作，在此之后若数组肯定是一样的，若值大于$0$就在操作一次，反之就不用操作了。

> $O(\sum n\times\log V)\\V=\max(a_i)-\min(a_i)$

```java
import java.io.*;
import java.util.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    public static void solve(){
        int n = sc.nextInt();
        int a[] = new int[n];
        int mx = 0, mn = (int)1e9;
        boolean odd = false, even = false;
        for(int i = 0; i < n; i ++){
            a[i] = sc.nextInt();
            mx = Math.max(mx, a[i]);
            mn = Math.min(mn, a[i]);
            if(a[i] % 2 == 0) even = true;
            else odd = true;
        }
        if(even && odd) {
            pw.println(-1);
            return;
        }
        Vector<Integer> ans = new Vector<>();
        while(mx > mn){
            int m = (mx + mn) >>> 1;
            ans.add(m);
            mx = 0; mn = (int)1e9;
            for(int i = 0; i < n; i ++) {
                a[i] = Math.abs(a[i] - m);
                mx = Math.max(mx, a[i]);
                mn = Math.min(mn, a[i]);
            }
        }
        if(mx > 0) ans.add(mx);
        if(ans.size() > 40){
            pw.println(-1);
            return;
        }
        pw.println(ans.size());
        for(int i : ans) pw.print(i + " ");
        pw.print("\n");
    }
    public static void main(String[] args) throws IOException {
        int T = sc.nextInt();
        while(T --> 0) solve();
        pw.flush();pw.close();
    }
}
```

