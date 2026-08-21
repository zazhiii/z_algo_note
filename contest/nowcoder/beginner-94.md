# 牛客小白月赛94

[牛客 82957/C](https://ac.nowcoder.com/acm/contest/82957/C)

一个长度为 $n$ 的数组 $a$，要**最大化** $a$ 的极差。

可以做如下操作任意次（前提是数组至少有两个数字）

选择一个正整数 $i (1≤i<n)$，接着将 $ai$ 与 $a_i+1$ 合并为一个数字，结果为二者的和。

即：将 $a_i$变为 $a_i+a_{i+1}$，然后删去 $a_{i+1}$，当然操作完后 $a$ 的长度也会减一。

最大能将数组极差变为多少

>    答案满足某个性质，枚举所有满足这个性质的情况
>
>    答案满足$min$ 为原数组中的某一个$a_i$，枚举所有$a_i$作为$min$的情况，$max$一定为$\sum_{k=1}^{i-1}a_k$或者$\sum_{k=i+1}^na_k$
>
>    求和部分用前缀和计算。

```java
import java.io.*;
import java.util.*;
public class Main {
	static Scanner sc = new Scanner(System.in);
	static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
	static int n, a[];
	static long s[];
	public static void main(String[] args) throws IOException{
		n = sc.nextInt();
		a = new int[n + 1];
		s = new long[n + 1];
		for(int i = 1; i <= n; i ++) {
			a[i] = sc.nextInt();
			s[i] = s[i - 1] + a[i];
		}
		long ans = s[n] - s[1] - a[1];// 第1个为极小值
		ans = Math.max(ans, s[n - 1] - a[n]); // n
		for(int i = 2; i <= n - 1; i ++) {// 2 ~ n-1
			ans = Math.max(ans, s[i - 1] - a[i]);
			ans = Math.max(ans, s[n] - s[i] - a[i]);
		}
		pw.print(ans);
		pw.flush();		
	}
}
```

链接：[牛客 82957/D](https://ac.nowcoder.com/acm/contest/82957/D)

有一个长度为 $n$ 的排列 $p$， $p$ 未知，已知数组 $a$。
其中：$a_i=gcd(p_1,p_2,...,p_i)$，也就是说，$a_i$​ 表示排列 $p$ 中前 $i$ 个数字的最大公约数。

将排列 $p$ 复原，无解输出$-1$

>    

