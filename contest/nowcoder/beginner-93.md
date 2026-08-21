# 牛客小白月赛93

 **B. 交换数字**

链接：[牛客 82401/B](https://ac.nowcoder.com/acm/contest/82401/B)

有两个长度均为 $n$且不包含前导零的数字 a,ba,ba,b ，现在他可以对这两个数字进行任意次操作： 

1. ​		选择一个整数 $1≤i≤n$ ,并交换 $a,b$ 的第 $i$ 位 。 

     请输出任意次操作后$a \times b$ 的最小值，由于答案可能很大，请对 $998244353$ 取模。

> 贪心

> 将一个数换为最大，另一个换为最小即可。
>
> 初始化最大最小数为$A=0、B=0$， 从前往后遍历，设第$i$个位置的数的较大较小值分别为为$a_i$和$b_i$，将较大值添加到$A$的后面$(A\times10 + a_i)$，较小值添加到$B$的后面$(B\times 10 +b_i)$，同时计算结果$(A\times10 + a_i)\times (B\times 10 +b_i)$，计算过程中不断mod。
>
> 这样不需要写交换的逻辑。
>
> $O(n)$

```java
import java.io.*;
import java.util.*;
public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static int n;
    static char[] s1, s2;
    static int mod = 998244353;
    public static void main(String[] args) throws IOException {
    	n = sc.nextInt();
    	s1 = sc.next().toCharArray();
    	s2 = sc.next().toCharArray();
    	long ans = 0, A = 0, B = 0;
    	for(int i = 0; i<n; i++) {
    		int a = Math.max(s1[i] - '0', s2[i] - '0');
    		int b  = Math.min(s1[i] - '0', s2[i] - '0');
    		ans = ( ((A * 10 + a)%mod) * ((B * 10 + b)%mod) ) % mod;
    		A = (A * 10 + a)%mod;
    		B = (B * 10 + b)%mod;
    	}
    	pw.print(ans);
    	pw.flush();
	}
}
```

**C. 老虎机**

链接：[牛客 82401/C](https://ac.nowcoder.com/acm/contest/82401/C)

老虎机游玩规则：共有三个窗口，每个窗口在每轮游玩过程中会等概率从图案库里选择一个图案，根据最后三个窗口中图案的情况获得相应的奖励。

 现在你设定了图案的数量为 $m$，没有相同的图案得 $a$ 元，一对相同的图案 $b$ 元，三个相同的图案 $c$ 元。

​	你想知道在你设定的规则下，单次游玩期望收益是多少？答案对 $998244353$ 取模。

​	根据 **逆元** 的定义，如果你最后得到的答案是形如 $\frac{a}{b}$ 的分数，之后你需要对 $p$ 取模的话，你需要输出 $(a×b^{mod−2}) mod \ p$ 来保证你的答案是正确的。

> 数学期望、快速幂

> 三种情况的期望：
>
> 1. 为$0$：$m \times (\frac{1}{m} \times \frac{m-1}{m}\times\frac{m - 2}{m}) \times a$
> 2. 为$2$：$m\times(3\times\frac{1}{m}\times\frac{1}{m}\times\frac{m-1}{m})\times b$
> 3. 为$3$：$m \times(\frac{1}{m}\times\frac{1}{m}\times\frac{1}{m})\times c$

```java
import java.io.*;
import java.util.*;
public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static long T, m, a, b, c;
    static int mod = 998244353;
    public static void main(String[] args) throws IOException {
    	T = sc.nextInt();
    	while(T --> 0) {
    		m = sc.nextLong();
    		a = sc.nextLong();
    		b = sc.nextLong();
    		c = sc.nextLong();
    		long u = ( (m - 1)*(m - 2)*a + 3*(m - 1)*b + c ) % mod; //防止超后面超Long
    		long d = m * m % mod;//防止超后面超Long
    		pw.println((u%mod) * (qpow(d, mod - 2)%mod) %mod);
    	}
    	pw.flush();
    }
	private static long qpow(long a, long n) {
		long ans = 1;
		while(n > 0) {
			if((n & 1) == 1) ans = (ans * a)%mod;
			a = (a*a)%mod;
			n >>= 1;
		}
		return ans%mod;
	}
}
```

