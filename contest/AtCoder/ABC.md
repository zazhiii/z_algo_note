# AtCoder Beginner Contest 记录

## ABC 350

**C - Sort**

[AtCoder abc350_c](https://atcoder.jp/contests/abc350/tasks/abc350_c)

> 模拟
>
> 第$i$个元素应该放在$A_i$的位置，遍历，不断将当前位置的元素换到对应的位置

```java
import java.util.*;
import java.io.*;
public class Main {
    static Scanner s = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    public static void main(String[] args){
        int n = s.nextInt();
        int[] a = new int[n+1];
        for(int i = 1; i <=n; i++) a[i] = s.nextInt();
        List<int[]> res = new ArrayList<>();
        int ans = 0;
        for(int i = 1; i <=n; i++) {
            while(a[i] != i){
                ans++;
                res.add(new int[]{i, a[i]});
                int l = i, r = a[i];
                int t = a[l];
                a[l] = a[r];
                a[r] = t;
            }
        }
        pw.println(ans);
        for (int[] re : res) {
            pw.println(re[0]+" "+re[1]);
        }
        pw.flush();
    }
}
```

**D - New Friends**

[AtCoder abc350_d](https://atcoder.jp/contests/abc350/tasks/abc350_d)

> 并查集
>
> 最后所有用户会形成若干个完全图，若每个集合人数为$num$，则每个集合最终好友对数为$num*(num-1)/2$，求和所有集合的好友对数，减去原来的好友对数，即答案。
>
> 遍历用户，若用户$i$的顶节点不在`Set`内，则记录该集合的好友对数
>
> **$num*(num-1)/2$ 会超`int`**！！！！！

```java
import java.util.*;
public class Main {
    static Scanner s = new Scanner(System.in);
    static int n, m, p[], size[], a, b;
    public static void main(String[] args) {
       n = s.nextInt();
       m = s.nextInt();
       int k = m;//记录一下m
       p = new int[n + 1];
       size = new int[n + 1];
       for(int i = 1; i <= n; i++) {
    	   p[i] = i;
    	   size[i] = 1;
       }
       while(m -- >0) {
    	   a = s.nextInt();
    	   b = s.nextInt();
    	   if(find(a)!=find(b)) {
    		   size[find(b)] += size[find(a)];
    		   p[find(a)] = find(b);
    	   }
       }
       long res = 0;
       Set<Integer> set = new HashSet<>();
       for(int i = 1; i<=n; i++) {
    	   if(!set.contains(find(i))) {
    		   set.add(find(i));
    		   int num = size[find(i)];
    		   res += 1l*(num)*(num-1)/2;
    	   }
       }
       System.out.print(res - k);
    }
	private static int find(int x) {
		if(p[x] != x) p[x] = find(p[x]);
		return p[x];
	}
}
```



## ABC 351

**c. Merge the balls**

[AtCoder abc351_c](https://atcoder.jp/contests/abc351/tasks/abc351_c)

> 模拟
>
> 对于每一个球：先将第$i$个球加入序列，记录幂级数，若最后两个球一样，则倒数第二个球的幂级数$+1$，直到停止操作。

```java
import java.util.*; 
public class Main {
    static Scanner s = new Scanner(System.in);
    static int n, a[], p = 0;
    public static void main(String[] args) {
       n = s.nextInt();
       a = new int[n + 1];
       for(int i = 1; i<=n; i++) {
    	   a[p ++] = s.nextInt();
    	   while(p >=2&&a[p - 1] == a[p - 2]) {
    		   a[p - 2] += 1;
    		   p--;
    	   }
       }
       System.out.print(p);
    }
}
```

[AtCoder abc351_d](https://atcoder.jp/contests/abc351/tasks/abc351_d)

> BFS求联通块

```java
import java.io.*;
import java.util.*;
public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static int n, m;
    static char a[][];
    static boolean vis[][];
    public static void main(String[] args) throws IOException {
        n = sc.nextInt();
        m = sc.nextInt();
        a = new char[n][m];
        vis = new boolean[n][m];
        for(int i = 0; i < n; i ++){
            a[i] = sc.next().toCharArray();
        }
        for(int i = 0; i < n; i ++){
            for(int j = 0; j < m; j ++){
                if(!vis[i][j] && a[i][j] == '.' && !stop(i, j)){
                    cnt = 0;
                    bfs(i, j);
                    ans = Math.max(ans, cnt);
                    while(!que2.isEmpty()){//清除磁铁旁标记，其他联通块可能搜到
                        int pos[] = que2.poll();
                        vis[pos[0]][pos[1]] = false;
                    }
                }
            }
        }
        pw.println(ans);
        pw.flush();
    }
    static int cnt, ans = 1;
    static Queue<int[]> que2 = new LinkedList<>();
    static int[] dx = {1, -1, 0, 0}, dy = {0, 0, 1, -1};
    private static void bfs(int x0, int y0) {
        Queue<int[]> que = new LinkedList<>();
        que.add(new int[]{x0, y0});
        vis[x0][y0] = true;
        cnt ++;
        while(!que.isEmpty()){
            int x, y, pos[];
            pos = que.poll();
            x = pos[0];
            y = pos[1];
            if(stop(x, y)) {
                que2.add(new int[]{x, y});
                continue;
            }
                for(int i = 0; i < 4; i ++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                if(nx >= 0 && nx < n && ny >= 0 && ny < m && a[nx][ny] == '.' && !vis[nx][ny]){
                    que.add(new int[]{nx, ny});
                    vis[nx][ny] = true;
                    cnt ++;
                }
            }
        }
    }
    private static boolean stop(int x, int y) {
        for(int i = 0; i < 4; i ++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(nx >= 0 && nx < n && ny >= 0 && ny < m && a[x + dx[i]][y + dy[i]] == '#'){
                return true;
            }
        }
        return false;
    }
}
```



## ABC 352

**D - Permutation Subsequence**

[AtCoder abc352_d](https://atcoder.jp/contests/abc352/tasks/abc352_d)

> **单调队列**、**区间最大值**
>
> 记录每个数的位置，按数大小排序，遍历，计算长度为$k$的连续序列中位置的最大值与最小值的差，记录最小值
>
> $P_i:$$10\ 1\ 6\ 8\ 7\ 2\ 5\ 9\ 3\ 4$			--->     $P_i:1\ 2\ 3\ 4\ 5\ 6\ 7\ 8\ 9\ 10$			--->      5 6 7 8 9	--->  $8 - 3 = 5$
>
> $i:\ \ 1\ \ 2\ 3\ 4\ 5\ 6\ 7\ 8\ 9\ 10 	$		            	$i : 2\ 6\ 9\ 10\ 7\ 3\ 5\ 4\ 8\ 1$				    7 3 5 4 8
>
> 区间内最大值最小值用**单调队列维护**

```java
import java.io.*;
import java.util.*;
public class Main {
    static Scanner s = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static Read r = new Read();
    static int n, k, a[], q[], min[], max[];
    public static void main(String[] args) throws IOException {
    	n = r.nextInt();
    	k = r.nextInt();
    	a = new int[n + 1];
    	q = new int[n + 1];
    	min = new int[n + 1];
    	max = new int[n + 1];
    	for(int i = 1; i<=n; i++) a[r.nextInt()] = i;
    	int hh = 0, tt = -1;
    	for(int i = 1; i<=n; i++) {
    		if(hh <= tt && q[hh] < i - k + 1) hh ++;
    		while(hh <= tt && a[q[tt]] >= a[i]) tt --;
    		q[ ++ tt] = i;
    		if(i >= k) min[i] = a[q[hh]];
    	}
    	hh = 0; tt = -1;
    	for(int i = 1; i<=n; i++) {
    		if(hh <= tt && q[hh] < i - k + 1) hh ++;
    		while(hh <= tt && a[q[tt]] <= a[i]) tt --;
    		q[ ++ tt] = i;
    		if(i >= k) max[i] = a[q[hh]];
    	}
    	int res = (int)1e6;
    	for(int i = k; i<=n; i++) res = Math.min(res, max[i] - min[i]);
    	pw.print(res);
	    pw.flush();
    }
}

class Read{
	StreamTokenizer st = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
	public int nextInt() throws IOException {
		st.nextToken();
		return (int)st.nval;
	}
}
```

## ABC 353

[C - Sigma Problem (atcoder.jp)](https://atcoder.jp/contests/abc353/tasks/abc353_c)

>    若不算$mod$操作求和为$(n-1)\times \sum A_i$，若两个数加起来大于了$10^8$，mod则会减去$10^8$。所以计算一下有多少对加起来大于$10^8$的数，然后求和减去这么多个$10^8$即可
>
>    遍历每一个数，对于当前数，**找右侧与他的和大于$10^8$的最小的数位置**，计算出对数。

```java
import java.io.*;
import java.util.*;
public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    public static void main(String[] args) throws IOException {
    	int mod = (int)1e8;
    	int n = sc.nextInt();
    	long a[] = new long[n + 1];
    	long sum = 0;
    	for(int i = 1; i<=n; i++) {
    		a[i] = sc.nextInt();
    		sum += a[i] * (n - 1);
    	}
    	Arrays.sort(a);
    	//查找有多少对 a[i] + a[j] >= mod
    	long cnt = 0;
    	for(int i = 1; i<=n - 1; i++) {
    		if(a[i] + a[i + 1] >= mod) {
    			cnt += n - i;
    		}else {
    			int l = i + 1, r = n, idx = n + 1;
    			while(l <= r) {
    				int m = (l + r) >>1;
    				if(a[m] >= mod - a[i]) {
    					idx = m;
    					r = m - 1;
    				}else {
    					l = m + 1;
    				}
    			}
    			cnt += n - idx + 1;
    		}
    	}
    	pw.print(sum - cnt * mod);
    	pw.flush();
    }
}
```

**D - Another Sigma Problem**

[D - Another Sigma Problem](https://atcoder.jp/contests/abc353/tasks/abc353_d)

>    快速幂

>    找一下有什么规律：3 14 15
>
>    $3\times10^2+14$
>
>    $+$
>
>    $(3+14)\times10^2+15\times2$
>
>    
>
>    $\sum_{i=1}^n\sum_{j=1}^{i-1}a_j\times 10^{len(a_i)}+a_i\times(i-1)$

```java
import java.io.*;
import java.util.*;
public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static int mod = 998244353;
    public static void main(String[] args) throws IOException {
    	int n = sc.nextInt();
    	long a[] = new long[n + 1];
    	for(int i = 1; i<=n; i++) a[i] = sc.nextLong();
    	long ans = 0, sum = a[1];
    	for(int i = 2; i<=n; i++) {
    		ans += sum * qpow(10, len(a[i])) % mod + a[i] * (i - 1) % mod;
    		sum = (sum + a[i]) % mod;
    	}
    	pw.print(ans % mod);
    	pw.flush();
    }
	private static long qpow(long a, long n) {
		long ans = 1;
		a %= mod;
		while(n > 0) {
			if( (n & 1) == 1) ans = (ans * a) % mod;
			a = a*a%mod;
			n >>= 1;
		}
		return ans;
	}
	private static long len(long n) {
		return (n+"").length();
	}
}

```

**E - Yet Another Sigma Problem**

[E - Yet Another Sigma Problem](https://atcoder.jp/contests/abc353/tasks/abc353_e) **字典树**

## ABC 354

[C - AtCoder Magics](https://atcoder.jp/contests/abc354/tasks/abc354_c)

高桥有纸牌游戏 "AtCoder Magics "中的 $N$ 张纸牌。其中的 $i$ 张卡将被称为 $i$ 张卡。每张卡都有两个参数：强度和成本。卡片 $i$ 的强度为 $A_i$ ，成本为 $C_i$ 。

他不喜欢弱牌，所以他会弃掉它们。具体来说，他会重复下面的操作，直到无法再进行为止：

- 选择两张牌 $x$ 和 $y$ ，即 $A_x > A_y$ 和 $C_x < C_y$ 。弃牌 $y$ 。

可以证明，当无法再进行操作时，剩下的牌的集合是唯一确定的。请找出这组牌。

>排序

>**注意看题！！！/(ㄒoㄒ)/~~**
>
>- $A_1,A_2,…,A_N$ are all distinct.
>- $𝐶_1,𝐶_2,…,𝐶_𝑁$are all distinct.
>
>每个卡牌按照$C_i$排序。对于第$i$张卡只需要比较$A_i$和$max(A_j),j\in[0,i-1]$即可直到是否应该被删除（因为已知$C_i>C_j$)。标记应该被删除的卡，在按照序号排序回来，输出答案。

```java
import java.io.*;
import java.util.*;
public class Main {
	static Scanner sc = new Scanner(System.in);
	static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
	static int n;
	static boolean st[];
	static class Card{
		int a, c, idx;
		boolean k;
	}
	static Card cards[];
	public static void main(String[] args) throws IOException{
		n = sc.nextInt();
		cards = new Card[n];
		st = new boolean[n];
		for(int i = 0; i < n; i ++) {
			Card card = new Card();
			card.a = sc.nextInt();
			card.c = sc.nextInt();
			card.idx = i + 1; 
			cards[i] = card;
		}
		Arrays.sort(cards, (c1, c2) -> c1.c - c2.c);
		int maxa = 0, ans = n;
		for(int i = 0; i < n; i++) {
			if(cards[i].a < maxa) {
				cards[i].k = true;
				ans --;
			}else {
				maxa = cards[i].a;
			}
		}
		pw.println(ans);
		Arrays.sort(cards, (c1, c2) -> c1.idx - c2.idx);
		for(int i = 0; i < n; i++) 
			if(!cards[i].k) pw.print((i + 1) + " ");
		pw.flush();
	}
}
```

## ABC 355

**D - Intersecting Intervals**

[AtCoder abc355_d](https://atcoder.jp/contests/abc355/tasks/abc355_d)

给你 $N$ 个实数区间。 $i$ $(1 \leq i \leq N)$ 区间为 $[l_i, r_i]$ 。求 $i$ -th 和 $j$ -th区间相交的 $(i, j),(1 \leq i < j \leq N)$ 对的个数。

>    排序 + 二分｜排序 + 扫描

> 法一：
>
> **当直接求不好求时，求对立情况来容斥出待求情况**

> 用不相交的区间对数容斥相交的区间
>
> $l_i$标记0，$r_i$标记1。按照左端点排序
>
> 遇到每一个左端点，若前面有$x$个结束了的区间则不相交对数$+x$
>
> $O(n)$

```java
    static int n;
    static List<int[]> p = new LinkedList<>();
    private static <T> void solve() throws IOException {
        n = rd.nextInt();
        for(int i = 1; i <= n; i ++){
            p.add(new int[]{rd.nextInt(), 0});
            p.add(new int[]{rd.nextInt(), 1});
        }
        //按照端点排序 注意处理开始点和结束点重合的情况
        Collections.sort(p, (p1, p2) -> p1[0] == p2[0] ? p1[1] - p2[1] : p1[0] - p2[0]);
        long ans = n*(n - 1l)/2;
        int ended = 0;
        for(int[] p : p){
            if(p[1] == 1) ended ++;
            else ans -= ended;
        }
        pw.println(ans);
    }
```

>    法二：二分
>
>    按左端点排序，枚举每一个线段$i$的右端点，二分找出最大且小于等于该右端点的左端点所在的线段$j$（即与该线段相交的最右侧的那一根线段），$ans = ans + j - i$。
>
>    $O(n \log n)$

```java
import java.io.*;
import java.util.*;
public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static int n, a[][];
    public static void main(String[] args) {
        n = sc.nextInt();
        a = new int[n][2];
        for(int i = 0; i < n; i ++){
            int l = sc.nextInt();
            int r = sc.nextInt();
            a[i] = new int[]{l, r};
        }
        Arrays.sort(a, (a1, a2) -> a1[0] - a2[0]);
        //枚举每一个右端点i，查找最大且<=该右端点的线段j ans += j - i
        long ans = 0;
        for(int i = 0; i < n; i ++){
            int cr = a[i][1];
            int l = i, r = n - 1, j = l;
            while(l <= r){
                int m = (r + l) >>> 1;
                if(a[m][0] <= cr){
                    j = m;
                    l = m + 1;
                }else{
                    r = m - 1;
                }
            }
            ans += j - i;
        }
        pw.println(ans);
        pw.flush();
    }
}
```



## ABC 356

[C - Keys](https://atcoder.jp/contests/abc356/tasks/abc356_c)

你有 $N$ 个编号为 $1, 2, \dots, N$ 的密钥。  其中一些是真钥匙，其他的是假钥匙。

有一扇门，门 X，你可以插入任意数量的钥匙。只有插入至少 $K$ 把真钥匙，X 门才会打开。

你已经对这些钥匙进行了 $M$ 次测试。 $i$ 次测试过程如下：

- 您将 $C_i$ 把 $A _{i,1}, A_{i,2}, \dots, A_{i,C_i}$ 把钥匙插入了 X 号门。
- 测试结果用一个英文字母 $R_i$ 表示。
    - $R_i =o$  表示在 $i$ \-th 测试中门 X 打开了。
    - $R_i=x$ 表示在 $i$ 次测试中，门X没有打开。

有 $2^N$ 种可能的钥匙组合，其中哪些是真钥匙，哪些是假钥匙。在这些组合中，找出与任何测试结果都不矛盾的组合数。  
给定的测试结果有可能是错误的，没有任何组合满足条件。在这种情况下，报告 $0$ 。

>    **二进制枚举**

>    $1\leq N \leq15$，考虑枚举所有钥匙的真假组合情况，再判断每一种情况是否满足所有测试，满足则答案数+1
>
>    $O(max(C_i)\times M\times2^N)$

```java
import java.io.*;
import java.util.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static int n, m, k, c[], a[][];
    static char r[];
    public static void main(String[] args) throws Exception {
        n = sc.nextInt();
        m = sc.nextInt();
        k = sc.nextInt();
        c = new int[m];
        r = new char[m];
        a = new int[m][15];
        for(int i = 0; i < m; i ++){
            c[i] = sc.nextInt();
            for(int j = 0; j < c[i]; j ++) a[i][j] = sc.nextInt();
            r[i] = sc.next().charAt(0);
        }
        int ans = 0;
        for(int i = 0; i < 1 << n; i ++){
            if(ok(i)) ans ++;
        }
        pw.println(ans);
        pw.flush();pw.close(); 
    }
    private static boolean ok(int i) {
        for(int j = 0; j < m; j ++){
            int t = 0;
            for(int k = 0; k < c[j]; k ++){
                //这里取位数要注意
                if( (i >> (a[j][k] - 1) & 1) == 1 ) t ++;
            }
            if(t >= k && r[j] == 'x') return false;
            if(t < k && r[j] == 'o') return false;
        }
        return true;
    }
}
```

## ABC 357

D	[AtCoder abc357_d](https://atcoder.jp/contests/abc357/tasks/abc357_d)

对于正整数 $N$ ，设 $V_N$ 是由 $N$ 恰好连接 $N$ 次所组成的整数。  
更确切地说，将 $N$ 视为一个字符串，将其连接 $N$ 份，并将结果视为一个整数，得到 $V_N$ 。  
例如， $V_3=333$ 和 $V_{10}=10101010101010101010$ 。

求 $V_N$ 除以 $998244353$ 的余数。

> **快速幂、逆元**

> 拼成：$NN...NNN$，$N$个$N$。
>
> 设$N$长度：$len$
>
> 从右往左第$k$个$N$的权值为$10^{(k -1)\times len}$
>
> 原式化为：$N\times (10^{(N-1)\times len}+10^{(N-2)\times len} +...+10^0)$
>
> 括号内为等比数列，用求和公式求和即可。$\frac{a_1(1-q^n)}{1-q}$
>
> $\frac{a}{b}$对$P$求模，$P$为质数，则：$\frac{a}{b} \mod P = a\times b^{p-2}\mod P$

```java
import java.io.*;
import java.util.*;
public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static long N, mod = 998244353;
    public static void main(String[] args) throws IOException {
        N = sc.nextLong();
        int len = (N + "").length();
        long q = qpow(10, len);
        long ans = N % mod * ((qpow(q, N) - 1) % mod * qpow(q - 1, mod - 2) % mod) % mod;
        pw.println(ans % mod);
        pw.flush();
    }
    public static long qpow(long a, long n){
        a %= mod;
        long ans = 1;
        while(n > 0){
            if((n & 1) == 1) ans = ans * a % mod;
            a = a * a % mod;
            n >>= 1;
        }
        return ans;
    }
}
```

## ABC 358

[B - Ticket Counter](https://atcoder.jp/contests/abc358/tasks/abc358_b)

游客排队逐个购票。每人购票需要 $A$ 秒。一旦排在队伍前面的人完成购票，下一个人（如果有的话）就会立即开始他们的购票过程。

目前，售票点没有人排队， $N$ 人会陆续前来购票。具体来说， $i$ th 人将在 $T_i$ 秒后到达售票点。如果已经有人排队，他们会排在队伍的最后；如果没有，他们会立即开始购票。这里， $T_1 \lt T_2 \lt \dots \lt T_N$ .

对于每个 $i\ (1 \leq i \leq N)$ ，确定从现在起 $i$ /th 的人将在多少秒后完成购票。

> 分类讨论

> 若$i$-th来时$i-1$-th已买完，则当前买完时间为来的时间+A
>
> 若$i$-th来时$i-1$-th没买完，则前面买完的时间 + A

```java
import java.io.*;
import java.util.*;
public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static int n, A;
    static long t[];
    public static void main(String[] args) throws Exception {
        n = sc.nextInt();
        A = sc.nextInt();
        t = new long[n + 1];
        for(int i = 1; i <= n; i ++){
            int x = sc.nextInt();
            if(x >= t[i - 1]) t[i] = x + A;
            else t[i] = t[i - 1] + A;
            pw.println(t[i]);
        }
        pw.flush();pw.close(); 
    }
}
```

[C - Popcorn](https://atcoder.jp/contests/abc358/tasks/abc358_c)

在 AtCoder 乐园里，有 $N$ 个爆米花摊位，编号从 $1$ 到 $N$ 。它们有 $M$ 种不同口味的爆米花，标号为 $1, 2, \dots, M$ ，但并不是每个摊位都出售所有口味的爆米花。

高桥获得了关于每个摊位都出售哪些口味爆米花的信息。这些信息由长度为 $M$ 的 $N$ 字符串 $S_1, S_2, \dots, S_N$ 表示。如果 $S_i$ 的 $j$ -th 字符是 "o"，则表示 $i$ 摊位销售的爆米花口味为 $j$ 。如果是 "x"，则表示 $i$ 摊位不出售 $j$ 口味的爆米花。每个摊位至少出售一种口味的爆米花，每种口味的爆米花至少在一个摊位上出售。

高桥想尝遍所有口味的爆米花，但又不想走动太多。求高桥至少要去多少个摊位才能买到所有口味的爆米花？

> **二进制枚举**

> 用二进制代表商店的售卖情况和选择商店的情况，见代码

```java
import java.io.*;
import java.util.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static int n, m, a[];
    public static void main(String[] args) throws Exception {
        n = sc.nextInt();
        m = sc.nextInt();
        a = new int[n];//二进制记录每个单位的售卖情况，例如：11100
        for(int i = 0; i < n; i ++){
            String s = sc.next();
            for(int j = 0; j < m; j ++){
                if(s.charAt(j) == 'o'){
                    a[i] |= 1 << j;//一个摊位中的某一种爆米花
                }
            }
        }
        int ans = 1 << n;
        //然后枚举店铺先与不选的情况，即二进制枚举用[0, 2^n - 1]表示
        for(int i = 0; i < 1 << n; i ++){
            int t = 0;//统计已经买到的爆米花
            for(int j = 0; j < n; j ++){//判断每一位是否为 1
                if((i >> j & 1) == 1){//若i的第j位为1，即要选择第j个店铺
                    t |= a[j];
                }
            }
            if(Integer.bitCount(t) == m){
                ans = Math.min(ans, Integer.bitCount(i));
            }
        }
        pw.println(ans);
        pw.flush();pw.close(); 
    }
}
```

[D - Souvenir](https://atcoder.jp/contests/abc358/tasks/abc358_d)

有 $N$ 盒子。编号为 $1$ 至 $N$ ，盒子 $i$ 的价格为 $A_i$ 日元，里面有 $A_i$ 块糖果。

从 $N$ 个盒子中买 $M$ 个，然后给 $M$ 个叫 $1, 2, \ldots, M$ 的人每人一盒。

满足以下条件：

- 对于每个 $i = 1, 2, \ldots, M$ 人， $i$ 都会得到一个至少装有 $B_i$ 块糖果的盒子。

请注意，不允许给一个人多个盒子，也不允许给多个人同一个盒子。

求是否可能买到满足条件的 $M$ 盒，如果可能，求高桥需要支付的最小总金额。

> **双指针**

> 类似判断子序列

```java
import java.io.*;
import java.util.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static int n, m, a[], b[];
    public static void main(String[] args) throws Exception {
        n = sc.nextInt();
        m = sc.nextInt();
        a = new int[n];
        b = new int[m];
        for(int i = 0; i < n; i ++) a[i] = sc.nextInt();
        for(int i = 0; i < m; i ++) b[i] = sc.nextInt();
        Arrays.sort(a);
        Arrays.sort(b);
        int i = 0, j = 0;
        long ans = 0;
        while(i < n && j < m){
            if(b[j] <= a[i]) {
                j ++;
                ans += a[i];
            }
            i ++;
        }
        pw.println(j == m ? ans : -1);
        pw.flush();pw.close(); 
    }
}
```

## ABC 359

**C**

<img src="images/image-20240624232531195.png" alt="image-20240624232531195" style="zoom: 25%;" />

> 思维

> 垂直距离为必须移动的距离，每移动一个垂直距离就可以多往两侧移动一个距离。
>
> 所以先移动垂直距离，在判断水平距离是否在通过垂直移动额外能移动的范围内，若不在，再加上需要移动的水平距离。
>
> 先预处理一下，将不用穿墙的能移动的先移动。

```java
import java.io.*;
import java.util.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    public static void main(String[] args) throws Exception {
        long a, b, c, d;
        a = sc.nextLong();
        b = sc.nextLong();
        c = sc.nextLong();
        d = sc.nextLong();
        if(a < c && a % 2 == b % 2) a ++;
        if(a < c && c % 2 != d % 2) c --;
        if(a > c && a % 2 != b % 2) a --;
        if(a > c && c % 2 == d % 2) c ++;
        long ans = 0;
        ans += Math.abs(b - d);
        ans += Math.max(0, Math.abs(a - c) - ans + 1) >> 1;
        pw.println(ans);
        pw.flush();pw.close(); 
    }
}
```

## ABC 360

[C - Move It (atcoder.jp)](https://atcoder.jp/contests/abc360/tasks/abc360_c)

有 $N$ 个箱子和 $N$ 件物品，编号均为 $1\sim N$。

第 $i$ 件物品放置在第 $A_i$ 个箱子中，重量为 $W_i$。

你可以将一件物品放置到另一个箱子里，而这件物品的重量就是这次操作的代价。

请问要让每个箱子都有一件物品至少要多少代价。

> 贪心

> 要让每个箱子有物品，必然从有多个物品的箱子将物品搬到空箱子（直到前者只剩一个物品）。其中搬轻的代价最小。
>
> ans = 总重量 -  每个箱子中最大重量

```java
import java.io.*;
import java.util.*;
public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static int n, a[], w[], max[];
    static long ans = 0;
    public static void main(String[] args) throws IOException {
        n = sc.nextInt();
        a = new int[n + 1];
        w = new int[n + 1];
        max = new int[n + 1];
        for(int i = 1; i <= n; i ++) a[i] = sc.nextInt();
        for(int i = 1; i <= n; i ++) w[i] = sc.nextInt();
        for(int i = 1; i <= n; i ++){
            max[a[i]] = Math.max(max[a[i]], w[i]);
            ans += w[i];
        }
        for(int i = 1; i <= n; i ++) ans -= max[i];
        pw.println(ans);
        pw.flush();pw.close();
    }
}
```

[D - Ghost Ants (atcoder.jp)](https://atcoder.jp/contests/abc360/tasks/abc360_d)

N只蚂蚁在数轴上，第$i$只蚂蚁的下标$X_i$，每只蚂蚁每秒向固定方向爬一格, $S_i$表示第i只蚂蚁的爬行方向：

$S_i=0$ 表示下标为$X_i$的蚂蚁面朝数轴负方向

$S_i=1$ 表示下标为$X_i$的蚂蚁面朝数轴正方向

若有两蚂蚁相遇，他们既不改变速度也不改变方向

请问在$T$秒以内，有多少蚂蚁相遇

> 二分、前缀和

> 对于每一个向左移动的蚂蚁$i$，能和它左侧离它$x_i - 2T$以内且向右移动的蚂蚁相遇。二分查找出大于等于目标坐标的最大坐标值，区间内所有的向右的蚂蚁数量用前缀和计算。

```java
import java.io.*;
import java.util.*;
public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static int n, T;
    static long a[][], pre[], ans = 0;
    static String s;
    public static void main(String[] args) throws IOException {
        n = sc.nextInt();
        T = sc.nextInt();
        s = sc.next();
        a = new long[n + 1][2];
        a[0][0] = -(long)2e18;
        for(int i = 1; i <= n; i ++){
            a[i][0] = sc.nextInt();
            a[i][1] = s.charAt(i - 1) - '0';
        }
        Arrays.sort(a, (e1, e2) -> e1[0] > e2[0] ? 1 : -1);
        pre = new long[n + 1];
        for(int i = 1; i <= n; i ++) pre[i] = pre[i - 1] + a[i][1];
        for(int i = 1; i <= n; i ++){
            if(a[i][1] == 0){
                int l = 1, r = i - 1, idx = i;
                while(l <= r){
                    int m = (r + l) >>> 1;
                    if(a[m][0] >= a[i][0] - 2 * T){
                        idx = m;
                        r = m - 1;
                    }else{
                        l = m + 1;
                    }
                }
                ans += pre[i] - pre[idx - 1];
            }
        }
        pw.println(ans);
        pw.flush();pw.close();
    }
}

```

## ABC 362

[D - Shortest Path 3 (atcoder.jp)](https://atcoder.jp/contests/abc362/tasks/abc362_d)

给定无向图 $N$ 个顶点 $M$ 条边. 每个顶点 $i\,(1\leq i \leq N)$ 有权重 $A_i$. 每条边 $j\,(1\leq j \leq M)$ 连接顶点 $U_j$ 和 $V_j$ 权重为 $B_j$. 该图中路径的权重定义为路径上出现的顶点和边的权重之和。

对于每一个顶点$i=2,3,\dots,N$, 求解: 

- 从顶点 $1$ 到顶点 $i$路径的最小权重。

> Dijkstra

> 板子题。对于每一个非起点的顶点，将其顶点的权重看作到该顶点的边的一部分即可。其余和djikstra一模一样。

> $O(m\log n)$

```java
import java.io.*;
import java.util.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static int n, m, a[];
    static long d[], inf = (long)1e18;
    static boolean vis[];
    static Vector<E>[] adj;
    static Queue<E> que = new PriorityQueue<>((o1, o2) -> o1.w > o2.w ? 1 : -1);
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
        //---dijkstra
        Arrays.fill(d, inf);
        d[1] = a[1];
        que.add(new E(1, d[1]));
        while(!que.isEmpty()){
            E p = que.poll();
            if(vis[p.v]) continue;
            vis[p.v] = true;
            for(E ne : adj[p.v]){
                if(d[ne.v] > d[p.v] + ne.w + a[ne.v]){
                    d[ne.v] = d[p.v] + ne.w + a[ne.v];
                    que.add(new E(ne.v, d[ne.v]));
                }
            }
        }
        for(int i = 2; i <= n; i ++) pw.print(d[i] + " ");
        pw.flush();pw.close();
    }
}
```

## ABC 363

[C - Avoid K Palindrome 2 ](https://atcoder.jp/contests/abc363/tasks/abc363_c)

> 全排列、枚举

```java
    public static boolean nextPermutation(char a[]){
        int n = a.length, i = n - 2;
        while(i >= 0 && a[i] >= a[i + 1]) i --;
        if(i < 0) return false;
        int k = i + 1;
        while(k < n && a[k] > a[i]) k ++;
        {char t = a[i]; a[i] = a[k - 1]; a[k - 1] = t;}// swap(a[i], a[k - 1])
        Arrays.sort(a, i + 1, n);
        return true;
    }
    static public void solve() throws IOException{
        int n = rd.nextInt();
        int k = rd.nextInt();
        char[] c = rd.next().toCharArray();
        Arrays.sort(c);
        int ans = 0;
        do{
            boolean ff = true;
            for(int i = k - 1; i < n; i ++){
                boolean f = true;
                for(int l = i - k + 1, r = i; l < r; l ++, r --){
                    if(c[l] != c[r]) {
                        f = false;
                        break;
                    }
                }
                if(f) ff = false;
            }
            if(ff) ans ++;
        }while(nextPermutation(c));
        pw.println(ans);
    }
```



[D - Palindromic Number (atcoder.jp)](https://atcoder.jp/contests/abc363/tasks/abc363_d)

求第$N$个为回文数的非负整数（$1\le N\le10^{18}$）

> 找规律
>
> 暂不考虑0，
>
> | 字符串长度 | 个数 |
> | :--------: | :--: |
> |     1      |  9   |
> |     2      |  9   |
> |     3      |  90  |
> |     4      |  90  |
> |     5      | 900  |
> |     6      | 900  |
> |     ……     |  ……  |
>
> 长度为$k$的回文串有$9\times10^{\lfloor\frac{k-1}{2}\rfloor}$个。
>
> 通过这个规律可以初步得到第$n$个回文串的长度。
>
> 接下来确定这个数具体是多少。
>
> 例如样例中的第 46 个回文数，初步确定长度为3（因为 46 比长度为1、2的回文串个数加起来还多）。
>
> 从前半段开始凑，第一个长度为3的回文数前半段（包括中间位置）为10(**10**1)，101是第一个长度为3的回文数，也是第1 （0是第一个）+ 9 + 9 + 1 = 20 个回文数，距离46还差26个回文数，在前半段 + 26得到第 46 个回文数的前半段：36，凑齐后半段结果为 363。
>
> 长度为偶数的回文数的凑法也类似。

```java
    static long[] t = new long[38];
    static{
        for(int i = 1; i <= 37; i ++){
            t[i] = 9 * (long) Math.pow(10, (i - 1) / 2);
            t[i] += t[i - 1];
        }
    }
    static public void solve() throws IOException{
        long n = rd.nextLong();
        int p = 0;
        while(t[p] < n) p ++;
        int preLen = (p + 1) / 2;
        long initPre = (long)Math.pow(10, preLen - 1);
        StringBuilder initPreSb = new StringBuilder((initPre + n - t[p - 1] - 2) + "");
        if(p % 2 == 1){
            pw.print(initPreSb.toString() + new StringBuilder(initPreSb.substring(0, initPreSb.length() - 1)).reverse());
        }else{
            StringBuilder t = new StringBuilder(initPreSb.toString());
            pw.print(t.append(initPreSb.reverse()));
        }
    }
```



## [ABC 364](https://atcoder.jp/contests/abc364/tasks)

[D - K-th Nearest (atcoder.jp)](https://atcoder.jp/contests/abc364/tasks/abc364_d)

在一条数线上有 $N+Q$ 个点 $A_1\dots,A_N,B_1,\dots,B_Q$ ，其中点 $A_i$ 的坐标为 $a_i$ ，点 $B_j$ 的坐标为 $b_j$ 。

就每个 $j=1,2,\dots,Q$ 回答下面的问题：

- 在$A_i$中离$B_j$第$k_j$近的点与$B_j$的距离。

> 二分答案

> 二分离$B_j$为$mid$的范围内有多少个点，若**刚好**有$k_j$个点且这个范围尽量小，那么这个距离则为所求距离。
>
> 如何求范围内有多少个点，直接遍历复杂度太高，将$a_i$排序，找到范围$[b_j-mid,b_j+mid]$中的最小值和最大值的索引即可算出该范围内有多少个数。这个寻找的过程也用二分实现。

> $O(q\times\log (2\times10^8)\times\log n)$

```java
import java.io.*;
import java.util.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static int n, q, a[], b, k;
    public static boolean check(int m, int b, int k){
        // [b - m, b + m]
        int l = lower_bound(a, 0, n - 1, b - m);
        int r = upper_bound(a, 0, n - 1, b + m);
        return r - l >= k;
    }                    
    public static void main(String[] args) throws IOException {
        n = sc.nextInt();
        q = sc.nextInt();
        a = new int[n];
        for(int i = 0 ; i < n; i ++) a[i] = sc.nextInt();
        Arrays.sort(a);
        while(q --> 0){
            b = sc.nextInt();
            k = sc.nextInt();
            int l = 0, r = (int)2e8, ans = 0;
            while(l <= r){
                int m = (l + r) >>> 1;
                if(check(m, b, k)){
                    ans = m;
                    r = m - 1;
                }else{
                    l = m + 1;
                }
            }            
            pw.println(ans);
        }
        pw.flush();pw.close();
    }
    public static int lower_bound(int a[], int l, int r, int t){
        int ans = r + 1;
        while(l <= r){
            int m = (l + r) >>> 1;
            if(a[m] >= t){ans = m; r = m - 1;}
            else l = m + 1;
        }
        return ans;
    }
    public static int upper_bound(int a[], int l, int r, int t){
        int ans = r + 1;
        while(l <= r){
            int m = (l + r) >>> 1;
            if(a[m] > t){ans = m; r = m - 1;}
            else l = m + 1;
        }
        return ans;
    }
}
```

## [ABC 365](https://atcoder.jp/contests/abc365/tasks)

[C - Transportation Expenses (atcoder.jp)](https://atcoder.jp/contests/abc365/tasks/abc365_c)

有 $N$ 人参加一项活动， $i$ /人的交通费用是 $A_i$ 日元。

活动组织者高桥（Takahashi）决定设定交通补贴的最高限额为 $x$ 。 $i$ 人的补贴为 $\min(x, A_i)$ 日元。这里， $x$ 必须是一个非负整数。

高桥的预算为 $M$ 日元，他希望所有 $N$ 人的交通补贴总额最多为 $M$ 日元，那么补贴限额 $x$ 的最大可能值是多少？

如果补贴限额可以无限大，请报告。

> 二分答案

> 二分$x$，判断支出是否大于$M$。找出最大的$x$且满足支出不超过$M$。若支付全部人的费用都不超过$M$那$x$就可以取无穷大
>
> **注意：输入Long**

> $O(N\times\log(\max A_i))$

```java
import java.io.*;
import java.util.*;

public class Prac {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static int n, a[];
    static long m;
    public static void main(String[] args) throws IOException {
        n = sc.nextInt();
        m = sc.nextLong();
        a = new int[n];
        int mx = 0;
        for(int i = 0; i < n; i ++){
            a[i] = sc.nextInt();
            mx = Math.max(mx, a[i]);
        }
        int l = 0, r = mx + 1, ans = 0;
        while(l <= r){
            int mid = (l + r) >>> 1;
            long sum = 0;
            for(int i = 0; i < n; i ++) sum += Math.min(mid, a[i]);
            if(sum <= m){
                ans = mid;
                l = mid + 1;
            }else{
                r = mid - 1;
            }
        }
        pw.println(ans == mx + 1 ? "infinite" : ans);
        pw.flush();pw.close();
    }

}
```

[D - AtCoder Janken 3](https://atcoder.jp/contests/abc365/tasks/abc365_d)

高桥和青木玩了 $N$ 次石头剪刀布。[注：在这个游戏中，石头赢剪刀，剪刀赢纸，纸赢石头。

青木的动作由长度为 $S$ 的字符串 $N$ 表示，字符串由 "R"、"P "和 "S "组成。 $i$ / $S$ 的字符表示青木在 $i$ / $i$ 对局中的棋步：R "表示 "石头"，"P "表示 "纸"，"S "表示 "剪刀"。

高桥的棋步满足以下条件：

- 高桥从未输给过青木。
- 对于 $i=1,2,\ldots,N-1$ ，高桥在 $i$ /th对局中的棋步与他在 $(i+1)$ /th对局中的棋步不同。

确定高桥可能赢得的最大对局数。

可以保证存在一个满足这些条件的高桥下棋顺序。

> 线性dp

> $dp[i][0|1|2]$：表示第$i$次出R、P、S能赢得局数。
>
> 状态转移：当前出的种类只能从前一次不一样的种类转移过来，且当前次不能出会输的种类。对于会输的种类将当前次初始化为负无穷，表示不能从这里转移出去。对于会赢的种类，加上前一次不一样的种类赢的次数的较大值再加1；对于会平局的种类，直接取前一次不同种类的赢得次数得较大值即可。

> $O(n)$

```java
import java.io.*;
import java.util.*;

public class Prac {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static int n, dp[][], inf = (int)1e9;
    static char c[];
    public static void main(String[] args) throws IOException {     
        n = sc.nextInt();
        dp = new int[n][3];//R P S
        c = sc.next().toCharArray();
        if(c[0] == 'R'){
            dp[0][0] = 0;
            dp[0][1] = 1;
            dp[0][2] = -inf;
        }
        if(c[0] == 'P'){
            dp[0][0] = -inf;
            dp[0][1] = 0;
            dp[0][2] = 1;
        }
        if(c[0] == 'S'){
            dp[0][0] = 1;
            dp[0][1] = -inf;
            dp[0][2] = 0;
        }
        for(int i = 1; i < n; i ++){
            if(c[i] == 'R'){
                dp[i][0] = Math.max(dp[i - 1][1], dp[i - 1][2]);
                dp[i][1] = Math.max(dp[i - 1][0], dp[i - 1][2]) + 1;
                dp[i][2] = -inf;
            }
            if(c[i] == 'P'){
                dp[i][0] = -inf;
                dp[i][1] = Math.max(dp[i - 1][0], dp[i - 1][2]);
                dp[i][2] = Math.max(dp[i - 1][0], dp[i - 1][1]) + 1;
            }
            if(c[i] == 'S'){
                dp[i][0] = Math.max(dp[i - 1][1], dp[i - 1][2]) + 1;
                dp[i][1] = -inf;
                dp[i][2] = Math.max(dp[i - 1][1], dp[i - 1][0]);
            }
        }
        pw.println(Math.max(dp[n - 1][0], Math.max(dp[n - 1][1], dp[n - 1][2])));
        pw.flush();pw.close();
    }
}
```

[E - Xor Sigma Problem (atcoder.jp)](https://atcoder.jp/contests/abc365/tasks/abc365_e)

给你一个长度为 $N$ 的整数序列 $A=(A_1,\ldots,A_N)$ 。求以下表达式的值：

$\displaystyle \sum_{i=1}^{N-1}\sum_{j=i+1}^N (A_i \oplus A_{i+1}\oplus \ldots \oplus A_j)$ .

> 前缀和、位运算

> 题目意思就是求每个长度不小于2的子串的异或和的和。
>
> 每个子串异或和可以用类似前缀和的方法求出。即假设$pre$是$a$的异或前缀和（$pre[i]=a_0\oplus a_1\oplus...\oplus a_i$）
>
> 可以证明：$a_i \oplus a_{i+1}\oplus...\oplus a_j=pre[j]\oplus pre[i-1](j\ge i)$
>
> 所有子串（包括长度为1的）的异或和之和就等于$pre$中的数两两异或之和。
>
> 由于位运算只与当前二进制位有关，我们可以分别考虑所有数的相同二进制位。
>
> 由于只有$0\oplus1$才会等于$1$，所以我们统计所有数该二进制位的$1和0$的个数，相乘就等于该位为最终答案在该位贡献了多少个$1$，再乘以该位的权重值（$2^{该位的位置}$），就是贡献的答案数。将所有位都计算一遍求和起来。
>
> 最后减去长度为$1$的字串的值（也就是每一个$a_i$）得到最终答案。
>
> 注意：答案用long存储

> $O(n\times\log V)$

```java
import java.io.*;
import java.util.*;

public class Prac {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static int n, a[], pre[];
    static long ans = 0;
    public static void main(String[] args) throws IOException {     
        n = sc.nextInt();
        a = new int[n + 1];
        pre = new int[n + 1];
        for(int i = 1; i <= n; i ++){
            a[i] = sc.nextInt();
            pre[i] = pre[i - 1] ^ a[i];
        }
        for(int k = 0; k < 32; k ++){
            int z = 0, o = 0;
            for(int i = 0; i <= n; i ++){
                if((pre[i] >> k) % 2 == 1) o ++;
                else z ++;
            }
            ans += (1l << k) * o * z;
        }
        for(int i = 1; i <= n; i ++) ans -= a[i];
        pw.println(ans);
        pw.flush();pw.close();
    }
}
```

## ABC 367

[D - Pedometer (atcoder.jp)](https://atcoder.jp/contests/abc367/tasks/abc367_d)

There are $N$ rest areas around a lake.  
The rest areas are numbered $1$, $2$, ..., $N$ in clockwise order.  
It takes $A_i$ steps to walk clockwise from rest area $i$ to rest area $i+1$ (where rest area $N+1$ refers to rest area $1$).  
The minimum number of steps required to walk clockwise from rest area $s$ to rest area $t$ ($s \neq t$) is a multiple of $M$.  
Find the number of possible pairs $(s,t)$.

> 前缀和

> 先把`[1, n]`的环拆成`[1, 2n - 1]`的链，即$a_1,a_2,...,a_n,a_1,...,a_{n-1}$。求$\sum_{i=l}^{r}a_i \bmod k = 0$的$l、r$对数。
>
> 求区间`[1, 2n - 1]`的前缀和`pre[]`，
>
> 即$(pre[r]-pre[l - 1])\bmod k= 0 \Rightarrow pre[r]\bmod k=pre[l-1]\bmod k$的答案数。
>
> 遍历`pre[]`用`map`记录某个数的出现次数，答案累加当前数在之前出现过的次数。
>
> **注意**：当目的地`i`是`[n + 1, 2n - 1]`之间时，只能从`[i - n + 1, n]`过来。

## [ABC 368](https://atcoder.jp/contests/abc368)

[C - Triple Attack](https://atcoder.jp/contests/abc368/tasks/abc368_c)

> 数学

```java
    static public void solve() throws IOException{
        int n = rd.nextInt();
        long ans = 0;
        for(int i = 1; i <= n; i ++){
            int x = rd.nextInt();
            ans += 1L * x / 5 * 3;
            x %= 5;
            while(x > 0){
                ans ++;
                x -= ans % 3 == 0 ? 3 : 1;
            }
        }
        pw.println(ans);
    }
```



## [ABC 370](https://atcoder.jp/contests/abc370)

[D - Cross Explosion (atcoder.jp)](https://atcoder.jp/contests/abc370/tasks/abc370_d)

二维网格，初始每个格子有墙。

依次进行$q$次放炸弹的操作，给定每次放炸弹的位置 $(i,j)$，如果该位置有墙，则该墙消失。

否则，炸弹会爆炸，会产生十字冲击波，该位置上下左右的各第一个墙都会消失。

问最后还存在的墙的数量

> **TreeSet**
>
> 用`TreeSet row[]`记录每行还剩哪些列的墙、`TreeSet col[]`记录每列还剩哪些行的墙。爆炸时，维护每个行、列的数量。
>
> 若爆炸时没有墙用`lower() higher()`函数判断上下左右是否有墙。**注意**：每次删除一个墙时需要维护该行该列的两个`TreeSet`

```java
import java.io.*;
import java.util.*;
public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(System.out);
    public static void solve(){
        int n = sc.nextInt();
        int m = sc.nextInt();
        int q = sc.nextInt();
        TreeSet<Integer>[] row = new TreeSet[n];
        TreeSet<Integer>[] col = new TreeSet[m];
        Arrays.setAll(row, i -> new TreeSet<>());   
        Arrays.setAll(col, i -> new TreeSet<>());   
        for(int i = 0; i < n; i ++){
            for(int j = 0; j < m; j ++){
                row[i].add(j);
                col[j].add(i);
            }
        }
        int ans = n * m;
        while(q --> 0){
            int x = sc.nextInt();
            int y = sc.nextInt();
            x --; y --;
            if(row[x].contains(y) && col[y].contains(x)){
                row[x].remove(y);
                col[y].remove(x);
                ans --;
            }else{
                Integer t;
                t = row[x].lower(y);
                if(t != null){
                    row[x].remove(t); 
                    col[t].remove(x);
                    ans --;
                }
                t = row[x].higher(y);
                if(t != null){
                    row[x].remove(t);
                    col[t].remove(x);
                    ans --;
                }
                t = col[y].lower(x);
                if(t != null){
                    col[y].remove(t); 
                    row[t].remove(y);
                    ans --;
                }
                t = col[y].higher(x);
                if(t != null){
                    col[y].remove(t);
                    row[t].remove(y);
                    ans --;
                }
            }
        }
        pw.println(ans);
    }
    public static void main(String args[]) throws IOException {
        solve();
        pw.flush();
    }   
}
```



## ABC 371

[C - Make Isomorphic (atcoder.jp)](https://atcoder.jp/contests/abc371/tasks/abc371_c)

将无向图$h$改为形状与无向图$g$相同的最小代价，在顶点$i、j$上加减边的代价为$A_{i,j}$。顶点个数$N\le8$

> 全排列
>
> 排列h的顶点，再枚举所有顶点，判断顶点之间的边的有无是否一致，不一致则修改。

```java
    public static void solve() throws IOException{     
        int n = rd.nextInt();
        boolean g[][] = new boolean[n + 1][n + 1];
        boolean h[][] = new boolean[n + 1][n + 1];
        int mg = rd.nextInt();
        while(mg --> 0){
            int u = rd.nextInt();
            int v = rd.nextInt();
            g[u][v] = g[v][u] = true;
        }
        int mh = rd.nextInt();
        while(mh --> 0){
            int u = rd.nextInt();
            int v = rd.nextInt();
            h[u][v] = h[v][u] = true;
        }

        int a[][] = new int[n + 1][n + 1];
        for(int i = 1; i < n; i ++){
            for(int j = i + 1; j <= n; j ++){
                a[i][j] = rd.nextInt();
                a[j][i] = a[i][j];
            }
        }

        int p[] = new int[n];
        for(int i = 1; i <= n; i ++) p[i - 1] = i;

        long ans = (long)1e18;
        do{
            long cnt = 0;
            for(int i = 1; i < n; i ++){
                for(int j = i + 1; j <= n; j ++){
                    if(h[p[i - 1]][p[j - 1]] ^ g[i][j]) cnt += a[p[i - 1]][p[j - 1]];
                }
            }

            ans = Math.min(ans, cnt);
        }while(next_permutation(p));

        pw.println(ans);
        
    }

    public static boolean next_permutation(int a[]){
        int n = a.length, i = n - 2;
        while(i >= 0 && a[i] > a[i + 1]) i --;
        if(i < 0) return false;
        int k = i + 1;
        while(k < n && a[k] > a[i]) k ++;
        int t = a[i]; a[i] = a[k - 1]; a[k - 1] = t;
        Arrays.sort(a, i + 1, n);
        return true;
    }
```

[D - 1D Country (atcoder.jp)](https://atcoder.jp/contests/abc371/tasks/abc371_d)

> 二分、前缀和

```java
    public static void solve() throws IOException{     
        int n = rd.nextInt();
        int x[] = new int[n + 1];
        long pre[] = new long[n + 1];
        for(int i = 1; i <= n; i ++) x[i] = rd.nextInt();
        for(int i = 1; i <= n; i ++) {
            pre[i] = rd.nextLong();
            pre[i] += pre[i - 1];
        }

        int q = rd.nextInt();
        while(q --> 0){
            int a = rd.nextInt();
            int b = rd.nextInt();
            int l = 1, r = n;
            while(l <= r){
                int m = (l + r) >>> 1;
                if(x[m] >= a) r = m - 1;
                else l = m + 1;
            }
            int L = l;
            l = 1; r = n;
            while(l <= r){
                int m = (l + r) >>> 1;
                if(x[m] <= b) l = m + 1;
                else r = m - 1;
            }
            int R = r;
            pw.println(pre[R] - pre[L - 1]);
        }
    }
```

[E - I Hate Sigma Problems (atcoder.jp)](https://atcoder.jp/contests/abc371/tasks/abc371_e)

> 考虑每一段子数组中每种数字的出现的第一个做出1个贡献（例如[**1**, 1, **2**, 2, **3**, **4**, **5**, 5]）。
>
> 那么在枚举每一个数$a_i$时，计算在多少个子数组中$a_i$是他这种数第一次出现的，用一个数组记录每一个数的上次出现的位置`st[x]`，那么包含$a_i$且他是他这种数第一次出现的子数组个数为`(i - st[x]) * (n - i + 1)`个（也就是枚举子数组起点和终点的总方案数），这是一个数做出的所有贡献，累加每一个数的贡献即为答案。

```java
    public static void solve() throws IOException{     
        int n = rd.nextInt();
        int st[] = new int[(int)2e5 + 10];
        long ans = 0;
        for(int i = 1; i <= n; i ++){
            int x = rd.nextInt();
            ans += 1L * (i - st[x]) * (n - i + 1);
            st[x] = i;
        }
        pw.println(ans);
    }
```

## [ABC 372](https://atcoder.jp/contests/abc372)

[D. Buildings](https://atcoder.jp/contests/abc372/tasks/abc372_d)

> 单调栈
>
> 倒序遍历元素，用单调栈维护当比前位置元素大的值，他们在当前位置的后方且单调不减，那么对于当前位置的答案就是这些元素的个数，即单调栈里元素的个数。
>
> $O(n)$

```java
    static public void solve() throws IOException{
        int n = rd.nextInt();
        int[] a = new int[n];
        for(int i = 0; i < n; i ++) a[i] = rd.nextInt();
        Deque<Integer> dq = new ArrayDeque<>();
        int[] ans = new int[n];
        for(int i = n - 1; i >= 0; i --){
            ans[i] = dq.size();
            while(!dq.isEmpty() && a[dq.peekLast()] < a[i]){
                dq.pollLast();
            }
            dq.addLast(i);
        }
        for(int i = 0; i < n; i ++) pw.print(ans[i] + " ");
    }
```

[E - K-th Largest Connected Components](https://atcoder.jp/contests/abc372/tasks/abc372_e)

> 并查集
>
> 操作2的意思是输出$v$节点所在联通块中第$k$大的节点。我们用`TreeSet`数组维护每一个连通块中的大小顺序，用并查集维护连通块，连通块的父节点的`TreeSet`维护这个连通块的大小顺序。在操作一合并连通块时，将两个连通块所维护的大小顺序也合并。若维护所有顺序全部合并的话会超时，注意到$k\le10$，我们只需要维护每个连通块的前10大的节点即可，合并的时候合并两个连通块的前10大节点，合并之后再删除后面十个节点。
>
> $O(Nk\log k)$

```java
    static int N = (int) 2e5 + 10;
    static int p[] = new int[N];
    static {
        for (int i = 0; i < N; i++)
            p[i] = i;
    }

    public static int find(int x) {
        if (p[x] != x)
            p[x] = find(p[x]);
        return p[x];
    }

    public static void union(int x, int y) {
        int fx = find(x), fy = find(y);
        if (fx != fy) {
            p[fx] = fy;
        }
    }

    static public void solve() throws IOException {
        int n = rd.nextInt();
        int q = rd.nextInt();
        TreeSet<Integer>[] ts = new TreeSet[N];
        Arrays.setAll(ts, i -> new TreeSet<Integer>((o1, o2) -> o2 - o1));
        for (int i = 1; i <= n; i++)
            ts[i].add(i);
        while (q-- > 0) {
            int t = rd.nextInt();
            if (t == 1) {
                int u = rd.nextInt();
                int v = rd.nextInt();
                ts[find(v)].addAll(ts[find(u)]);
                union(u, v);
                while (ts[v].size() > 10) {
                    ts[v].pollLast();
                }
            } else {
                int u = rd.nextInt();
                int k = rd.nextInt();
                int fu = find(u);
                if (ts[fu].size() < k) {
                    pw.println(-1);
                } else {
                    int p = 1;
                    for (int x : ts[fu]) {
                        if (p++ == k) {
                            pw.println(x);
                        }
                    }
                }
            }
        }
    }
```



## [ABC385](https://atcoder.jp/contests/abc385)

[C - Illuminate Buildings](https://atcoder.jp/contests/abc385/tasks/abc385_c)

> 枚举

```java
    static public void solve() throws IOException {
        int n = rd.nextInt();
        int[] a = new int[n];
        for(int i = 0; i < n; i ++) a[i] = rd.nextInt();
        int ans = 1; // fix
        for(int i = 0; i < n; i ++){
            for(int j = 1; j <= i; j ++){
                int cnt = 1;
                for(int k = i - j; k >= 0 && a[k] == a[i]; k -= j){
                    cnt ++;
                }
                ans = Math.max(ans, cnt);
            }
        }
        pw.println(ans);
    }
```





## [ABC386](https://atcoder.jp/contests/abc386)

[D - Diagonal Separation](https://atcoder.jp/contests/abc386/tasks/abc386_d)

> 排序
>
> 每个白色的右下方不能有黑色方块。
>
> 按照x为第一字段、y为第二字段排序。遍历所有点，记录出现的白色的最小y值$\min y$，后续的黑块的x必定大于出现的白色块的x，只需判断黑块的y值是否大于等于$\min y$。

```java
    static public void solve() throws IOException {
        int n = rd.nextInt();
        int m = rd.nextInt();
        List<int[]> a = new ArrayList<>();
        while(m --> 0){
            int x = rd.nextInt();
            int y = rd.nextInt();
            String op = rd.next();
            a.add(new int[]{x, y, op.equals("W") ? 0 : 1});
        }
        Collections.sort(a, (o1, o2) -> o1[0] == o2[0] ? o1[1] - o2[1] : o1[0] - o2[0]);
        int minWhiteY = n + 1; 
        for(int[] t : a){
            if(t[2] == 0){
                minWhiteY = Math.min(minWhiteY, t[1]);
            }else{
                if(t[1] >= minWhiteY){
                    pw.println("No");
                    return;
                }
            }
        }
        pw.println("Yes");
    }
```

[E - Maximize XOR](https://atcoder.jp/contests/abc386/tasks/abc386_e)

> DFS、剪枝
>
> 若$k\le n-k$，则DFS选$C_n^k$，否则选$C_n^{n-k}$。虽然结果数相同，但是递归深度不同。

```java
    static long ans = 0, a[], xor = 0;
    static int n, k;
    static public void solve() throws IOException {
        n = rd.nextInt();
        k = rd.nextInt();
        a = new long[n];
        for (int i = 0; i < n; i++) {
            a[i] = rd.nextLong();
            xor ^= a[i];
        }
        dfs(0, 0, 0);
        pw.println(ans);
    }
    public static void dfs(int x, int cnt, long sum) {
        if (cnt == k) {
            ans = Math.max(ans, sum);
            return;
        }
        if (cnt == n - k) {
            ans = Math.max(ans, xor ^ sum);
            return;
        }
        for(int i = x; i < n; i ++){
            dfs(i + 1, cnt + 1, sum ^ a[i]);
        }
    }
```





## [ABC 387](https://atcoder.jp/contests/abc387)

[AtCoder abc387_c](https://atcoder.jp/contests/abc387/tasks/abc387_c)

>    数位 dp

```java
    static long[][][] dp = new long[20][11][2];
    public static void clear(){
        for(int i = 0; i < 20; i ++){
            for(int j = 0; j < 11; j ++){
                dp[i][j][0] = dp[i][j][1] = -1;
            }
        }
    }
    static public void solve() throws IOException{
        long a = rd.nextLong();
        long b = rd.nextLong();
        pw.println(f(b) - f(a - 1));
    }
    public static long f(long num){
        int len = 1;
        long tmp = num / 10, offset = 1;
        while(tmp > 0){
            len ++;
            offset *= 10;
            tmp /= 10;
        }
        clear();
        return dfs(num, len, offset, 10, 0);
    }
    public static long dfs(long num, int len, long offset, int fst, int free){
        if(len == 1 && fst == 10){
            return 0;
        }
        if(len == 0){
            return 1;
        }
        if(dp[len][fst][free] != -1){
            return dp[len][fst][free];
        }
        long ans = 0;
        int cur = (int)(num / offset % 10);
        if(free == 0){
            if(fst == 10){ // 选第一个数
                ans += dfs(num, len - 1, offset / 10, 10, 1); // 第一个数不选
                for(int i = 1; i < cur; i ++){ // 首位已经决定小于num了
                    ans += dfs(num, len - 1, offset / 10, i, 1);
                }
                ans += dfs(num, len - 1, offset / 10, cur, 0);
            }else{ // 前面选得和 num 前缀一样
                for(int i = 0; i < cur && i < fst; i ++){
                    ans += dfs(num, len - 1, offset / 10, fst, 1);
                }
                if(cur < fst){
                    ans += dfs(num, len - 1, offset / 10, fst, 0);
                }
            }
        }else{
            if(fst == 10){ // 最高位没选且前面都没选
                ans += dfs(num, len - 1, offset / 10, 10, 1); // 继续不选
                for(int i = 1; i <= 9; i ++){
                    ans += dfs(num, len - 1, offset / 10, i, 1);
                }
            }else{ // 前面选了，已经确定比 num 小了
                for(int i = 0; i < fst; i ++){
                    ans += dfs(num, len - 1, offset / 10, fst, 1);
                }
            }
        }
        dp[len][fst][free] = ans;
        return ans;
    }
```



[D - Snaky Walk](https://atcoder.jp/contests/abc387/tasks/abc387_d) 

> BFS
>
> 每个状态记录四个字段：`x, y, step, flag` ： 位置、到该位置的步长、下一步可以走到方向（横/竖）

```java
    static public void solve() throws IOException{
        int n = rd.nextInt();
        int m = rd.nextInt();
        char[][] a = new char[n][m];
        Queue<int[]> que = new ArrayDeque<>();
        boolean[][][] vis = new boolean[n][m][2];
        for(int i = 0; i < n; i ++){
            a[i] = rd.next().toCharArray();
            for(int j = 0; j < m; j ++){
                if(a[i][j] == 'S') {
                    que.add(new int[]{i, j, 0, 0}); // x y step flag 
                    que.add(new int[]{i, j, 0, 1});
                    vis[i][j][0] = vis[i][j][1] = true;
                }
            }
        }
        int[] dx = {1, -1, 0, 0}, dy = {0, 0, 1, -1};
        while(!que.isEmpty()){
            int[] t = que.poll();
            int x = t[0], y = t[1], step = t[2], flag = t[3];
            if(a[x][y] == 'G'){
                pw.println(step);
                return;
            }
            if(flag == 0){
                for(int k = 0; k < 2; k ++){
                    int nx = x + dx[k];
                    int ny = y + dy[k];
                    if(nx >= 0 && nx < n && ny >= 0 && ny < m && !vis[nx][ny][1] && a[nx][ny] != '#'){
                        que.add(new int[]{nx, ny, step + 1, 1});
                        vis[nx][ny][1] = true;
                    }
                }
            }else{
                for(int k = 2; k < 4; k ++){
                    int nx = x + dx[k];
                    int ny = y + dy[k];
                    if(nx >= 0 && nx < n && ny >= 0 && ny < m && !vis[nx][ny][0] && a[nx][ny] != '#'){
                        que.add(new int[]{nx, ny, step + 1, 0});
                        vis[nx][ny][0] = true;
                    }
                }
            }
        }
        pw.println(-1);
    }
```

## [ABC 388](https://atcoder.jp/contests/abc388)



[C - Various Kagamimochi](https://atcoder.jp/contests/abc388/tasks/abc388_c)

> 二分 | 双指针

```java
    // 双指针
 	static public void solve() throws IOException{
        int n = rd.nextInt();
        int[] a = new int[n];
        long ans = 0;
        for(int i = 0; i < n; i ++) a[i] = rd.nextInt();
        Arrays.sort(a);
        for(int l = 0, r = 0; r < n; r ++){
            while(a[l] <= a[r] / 2){
                l ++;
            }
            ans += l;
        }
        pw.println(ans);
    }
	// 二分
    static public void solve() throws IOException{
        int n = rd.nextInt();
        int[] a = new int[n];
        long ans = 0;
        for(int i = 0; i < n; i ++) a[i] = rd.nextInt();
        Arrays.sort(a);
        for(int i = 0; i < n; i ++){
            int l = 0, r = i - 1;
            while(l <= r){
                int m = (l + r) >> 1;
                if(a[m] <= a[i] / 2) l = m + 1;
                else r = m - 1;
            }
            ans += r + 1;
        }
        pw.println(ans);
    }
```

[D - Coming of Age Celebration](https://atcoder.jp/contests/abc388/tasks/abc388_d)

> 差分

```java
    static public void solve() throws IOException{
        int n = rd.nextInt();
        long[] a = new long[n + 2];
        long[] b = new long[n + 2];
        for(int i = 1; i <= n; i ++) {
            a[i] = rd.nextInt();
            b[i] += b[i - 1];
            a[i] += b[i];
            b[i + 1] ++;
            b[(int)Math.min(n, i + a[i]) + 1] --;
            a[i] -= Math.min(n - i, a[i]);
            pw.print(a[i] + " ");
        }
    }
```

[E - Simultaneous Kagamimochi](https://atcoder.jp/contests/abc388/tasks/abc388_e)

> 贪心？
>
> 先排序，将所有数平分为两段(n / 2)，拿左边的每一个去和右边的匹配，直到左边的数用完或者右边的数用完。

```java
    static public void solve() throws IOException {
        int n = rd.nextInt();
        int[] a = new int[n];
        for(int i = 0; i < n; i ++) a[i] = rd.nextInt();
        Arrays.sort(a);
        int p = 0;
        int l = 0, r = n - 1;
        while (l <= r) {
            int m = (l + r) >>> 1;
            if(a[0] <= a[m] / 2) r = m - 1;
            else l = m + 1;
        }
        p = Math.max(n / 2, l); // 只去匹配右半部分的数
        l = 0; r = p;
        int ans = 0;
        for(int i = 0; i < p; i ++){
            while(r < n && a[i] > a[r] / 2){
                r ++;
            }
            if(r < n){
                ans ++;
                r ++;
            }
        }
        pw.println(ans);
    }
```



## [ABC391](https://atcoder.jp/contests/abc391)



[E - Hierarchical Majority Vote](https://atcoder.jp/contests/abc391/tasks/abc391_e)

>    dp
>
>    从长推到短，记录每个节点的「字符」和「要使当前字符改变的最小操作次数」
>
>    初始化：一开始每个节点的字符确定，修改当前字符的最小操作为 1
>
>    转移：由上面三个节点转移到一个节点，分别讨论 0、1 个数对两个信息的影响，转移到长度只有 1 时结束。
>
>    ```tex
>    sample_1
>    010011101 (111111111)
>    011(111)
>    1(1)
>    
>    sample_2
>    000(111)
>    1(2)
>    ```

```java
    static public void solve() throws IOException {
        int n = rd.nextInt();
        char[] c = rd.next().toCharArray();
        int[] cost = new int[c.length];
        Arrays.fill(cost, 1);
        pw.println(dfs(c, cost, n));

    }

    public static int dfs(char[] c, int[] cost, int n) {
        if (n == 0) return cost[0]; // 退出
        for (int i = 0; i < Math.pow(3, n - 1); i++) {
            int x = i * 3; int y = i * 3 + 1; int z = i * 3 + 2;
            int one = 0, maxOneCost = 0, minOneCost = inf;
            int zero = 0, maxZeroCost = 0, minZeroCost = inf;
            for (int j = x; j <= z; j++) {
                if (c[j] == '1') {
                    one++;
                    maxOneCost = Math.max(maxOneCost, cost[j]);
                    minOneCost = Math.min(minOneCost, cost[j]);
                } else {
                    zero++;
                    maxZeroCost = Math.max(maxZeroCost, cost[j]);
                    minZeroCost = Math.min(minZeroCost, cost[j]);
                }
            }
            if (one == 3 || one == 2) {
                c[i] = '1';
                if (one == 3) cost[i] = cost[x] + cost[y] + cost[z] - maxOneCost;
                if (one == 2) cost[i] = minOneCost;
            } else {
                c[i] = '0';
                if (zero == 3) cost[i] = cost[x] + cost[y] + cost[z] - maxZeroCost;
                if (zero == 2) cost[i] = minZeroCost;
            }
        }
        return dfs(c, cost, n - 1);
    }
```



## [ABC392](https://atcoder.jp/contests/abc392)

[D - Doubles](https://atcoder.jp/contests/abc392/tasks/abc392_d)

>    枚举、概率
>
>    预处理每个骰子的每个数出现几次 ，$cnt[i][x]$ ：第$i$个骰子中$x$出现几次。枚举每对骰子，再枚举其中一个$i$的每一个数$x$，若另一个骰子$j$中若包含$x$，那么可以计算概率$\frac{cnt[i][x]}{k_i}\times \frac{cnt[j][x]}{k_j}$，累加每个数的概率得到这对骰子 roll 到相同数的概率。

```java
        Map<Integer, Integer>[] map = new Map[n];
        Arrays.setAll(map, i -> new HashMap<>());
        int[] k = new int[n];
        int[] mxa = new int[n];
        double ans = 0;
        for(int i = 0; i < n; i ++){
            k[i] = rd.nextInt();
            for(int j = 0; j < k[i]; j ++){
                int x = rd.nextInt();
                map[i].put(x, map[i].getOrDefault(x, 0) + 1);
                mxa[i] = Math.max(mxa[i], x);
            }
            for(int j = 0; j < i; j ++){
                double res = 0;
                for(int x : map[i].keySet()){
                    if(map[j].containsKey(x)){
                        res += (1d * map[i].get(x) * map[j].get(x)) / (1d * k[i] * k[j]);
                    }
                }
                ans = Math.max(ans, res);
            }
        }
        pw.printf("%.15f", ans);
```



## [ABC 393](https://atcoder.jp/contests/abc393)

[D - Swap to Gather](https://atcoder.jp/contests/abc393/tasks/abc393_d)

> 贪心
>
> 让所有 1 聚成一堆也就是让所有 0 靠边站，对于每个 0 要么靠左要么靠右站，每个 0 靠边站和他左右有多少 0 以及他自己的位置有关，哪边需要移动步数少就往哪边移动
>
> $O(n)$

```java
    static public void solve() throws IOException {
        int n = rd.nextInt();
        char[] c = rd.next().toCharArray();
        long ans = 0;
        int[] l = new int[n], r = new int[n];
        for (int i = 1; i < n; i++)
            l[i] = l[i - 1] + (c[i - 1] == '0' ? 1 : 0);
        for (int i = n - 2; i >= 0; i--)
            r[i] = r[i + 1] + (c[i + 1] == '0' ? 1 : 0);
        for (int i = 0; i < n; i++)
            if (c[i] == '0')
                ans += Math.min(i - l[i], n - 1 - i - r[i]);
        pw.println(ans);
    }
```



## [ABC 394](https://atcoder.jp/contests/abc394)

[E - Palindromic Shortest Path](https://atcoder.jp/contests/abc394/tasks/abc394_e)

>    BFS
>    从最短的回文串路径「延长」出去的路径一定是回文串路径。初始化长度为 0 和 1 的回文串路径，利用 BFS 枚举 i、j 位置将每一个已经确定的最短回文串路径延长出去。从短到长地延长出去一定是最短回文串路径。
>
>    $O(n^4)$

```java
    static public void solve() throws IOException{
        int n = rd.nextInt();
        char[][] G = new char[n][n];
        Queue<int[]> que = new ArrayDeque<>();
        for(int i = 0; i < n; i ++){
            G[i] = rd.next().toCharArray();
        }
        int[][] ans = new int[n][n];
        for(int[] t : ans) Arrays.fill(t, -1);
        for(int i = 0; i < n; i ++){
            ans[i][i] = 0;
            que.add(new int[]{i, i, 0});
        }
        for(int i = 0; i < n; i ++){
            for(int j = 0; j < n; j ++){
                if(G[i][j] != '-' && i != j){
                    que.add(new int[]{i, j});
                    ans[i][j] = 1;
                }
            }
        }
        while(!que.isEmpty()){
            int[] t = que.poll();
            int x = t[0], y = t[1];
            for(int i = 0; i < n; i ++){
                for(int j = 0; j < n; j ++){
                    if(G[i][x] == G[y][j] && G[i][x] != '-' && ans[i][j] == -1){
                        que.add(new int[]{i, j});
                        ans[i][j] = ans[x][y] + 2;
                    }
                }
            }
        }
        for(int i = 0; i < n; i ++){
            for(int j = 0; j < n; j ++){
                pw.print(ans[i][j] + (j == n - 1 ? "\n" : " "));
            }
        }
    }
```



## [ABC 395](https://atcoder.jp/contests/abc395)

[C - Shortest Duplicate Subarray](https://atcoder.jp/contests/abc395/tasks/abc395_c)

>    记录每一个数前一次出现的位置$pre_i$，答案为$\min(i-pre_i+1)$

```java
    static public void solve() throws IOException{
        int n = rd.nextInt();
        Map<Integer, Integer> map = new HashMap<>();
        int ans = inf;
        for(int i = 0; i < n; i ++){
            int x = rd.nextInt();
            if(map.containsKey(x)){
                ans = Math.min(ans, i - map.get(x) + 1);
            }
            map.put(x, i);
        }
        pw.println(ans == inf ? -1 : ans);
    }
```

[D - Pigeon Swap](https://atcoder.jp/contests/abc395/tasks/abc395_d)

```java
    static public void solve() throws IOException{
        int n = rd.nextInt();
        int q = rd.nextInt();
        int[] f = new int[n + 1]; // 第 i 号巢放在第几个位置
        int[] g = new int[n + 1]; // 第 i 个位置放的是第几号巢
        int[] h = new int[n + 1]; // 第 i 个鸽子在第几个位置
        for(int i = 0; i <= n; i ++){
            f[i] = g[i] = h[i] = i;
        }
        while(q -- > 0){
            int op = rd.nextInt();
            int a = rd.nextInt();
            if(op == 1){
                int b = rd.nextInt();
                h[a] = f[b];
            }else if(op == 2){
                int b = rd.nextInt();
                g[f[a]] = b;
                g[f[b]] = a;
                int t = f[a];
                f[a] = f[b];
                f[b] = t;
            }else{
                pw.println(g[h[a]]);
            }
        }
    }
```

[E - Flip Edge](https://atcoder.jp/contests/abc395/tasks/abc395_e)

> 分图层最短路

```java
    static public void solve() throws IOException{
        int n = rd.nextInt();
        int m = rd.nextInt();
        int x = rd.nextInt();
        List<int[]>[] adj = new ArrayList[n + 1];
        Arrays.setAll(adj, i -> new ArrayList<>());
        while(m -- > 0){
            int u = rd.nextInt();
            int v = rd.nextInt();
            adj[u].add(new int[]{v, 1});
            adj[v].add(new int[]{u, -1});
        }
        long[][] d = new long[n + 1][2]; // d[i][0/1]：到 i 且状态为 未反转/反转 的最短路
        for(long[] t : d) Arrays.fill(t, INF);
        boolean[][] f = new boolean[n + 1][2];
        PriorityQueue<long[]> pq = new PriorityQueue<>((o1, o2) -> o1[2] >= o2[2] ? 1 : -1);
        d[1][0] = 0;
        d[1][1] = x;
        pq.add(new long[]{1L, 0L, d[1][0]});
        pq.add(new long[]{1L, 1L, d[1][1]});
        while(!pq.isEmpty()){
            long[] t = pq.poll();
            int u = (int)t[0]; int isRev = (int)t[1]; 
            if(f[u][isRev]) continue;
            f[u][isRev] = true;
            for(int[] vv : adj[u]){
                int v = vv[0], w = vv[1];
                if(isRev == 0){
                    if(w == 1){
                        if(d[u][0] + 1 < d[v][0]){
                            d[v][0] = d[u][0] + 1;
                            pq.add(new long[]{v, 0L, d[v][0]});
                        }
                    }else{
                        if(d[u][0] + 1 + x < d[v][1]){
                            d[v][1] = d[u][0] + 1 + x;
                            pq.add(new long[]{v, 1L, d[v][1]});
                        }
                    }
                }else{
                    if(w == 1){
                        if(d[u][1] + 1 + x < d[v][0]){
                            d[v][0] = d[u][1] + 1 + x;
                            pq.add(new long[]{v, 0L, d[v][0]});
                        }
                    }else{
                        if(d[u][1] + 1 < d[v][1]){
                            d[v][1] = d[u][1] + 1;
                            pq.add(new long[]{v, 1L, d[v][1]});
                        }
                    }
                }
            }
        }
        pw.println(Math.min(d[n][0], d[n][1]));
    }
```
