# 牛客周赛 Round 41

**B.小红的排列构造**

[牛客 80742/B](https://ac.nowcoder.com/acm/contest/80742/B)

定义两个数组$a$和$b$的汉明距离为：有多少个下标$i$满足$a_i≠b_i$。例如，$[2,3,1]$和$[1,3,1]$的汉明距离是$1$。
 现在小红拿到了一个长度为$n$的排列$p$，她希望你构造一个长度为$n$的排列$q$，满足$p$和$q$的汉明距离恰好等于$k$。

 排列指长度为$n$的数组，其中$1$到$n$每个元素恰好出现了一次

> 若$k > n $ 或者$k=1$，显然无解。
>
> 因为每个元素都只出现一次，交换两个无汉明距离的元素必定产生增加汉明距离， 交换一个有汉明距离的元素和一个无汉明距离的元素必定增加一个汉明距离。
>
> 遍历序列，设第$i$个数为$a_i$，不断让$a_i$和$a_{i+1}$交换，交换$k-1$次即可。
>
> ——第一次交换产生 2 个距离，后面每一次产生 1 个距离。

```java
import java.util.*;
public class Main {
    static Scanner s = new Scanner(System.in);
    static int n, k, a[];
    public static void main(String[] args){
    	n = s.nextInt();
    	k = s.nextInt();
    	a = new int[n];
    	if(k > n || k == 1) {
    		System.out.print(-1);
    		return;
    	}
    	for(int i = 0; i<n; i++) a[i] = s.nextInt();
    	for(int i = 0; i<=k - 2; i++) {
    		int t = a[i];
    		a[i] = a[i + 1];
    		a[i + 1] = t;
    	}
    	for(int i = 0; i<n; i++) System.out.print(a[i] + " ");
    }
}
```

**C. 小红的循环移位**

[牛客 80742/C](https://ac.nowcoder.com/acm/contest/80742/C)

小红拿到了一个数字串，她每次操作可以使得其向左循环移动一位。
 将串 $s=s_0s_1...s_{n−1}$​ 向左循环移动一位，将得到串$s_1...s_{n−1}s_0$
 小红想知道，使得该数字串变成4的倍数，需要最少操作多少次？（可以包含前导零）

> 枚举一下 4 的倍数：4  8  **12  16  20  24  28  32  36  40 44 ......**
>
> 发现规律：若数字位数大于1位，若个位数字为 2/6且高一位为奇数，则为4的倍数；若个位数字为4/8/0且高一位为偶数，则为4的倍数。
>
> 有了该规律就可以遍历一遍的情况下找出最小操作次数。
>
> 1. 特判一下一位数
> 2. 先判断 0 次操作是否可行。
> 3. 再判断$1 \sim n-1$次操作，设$a_i$为从左往右第$i$位数字，若$a_i$与$a_{i - 1}$满足规律，则需要操作$i$次
> 4. 若都不行则输出$ - 1$
>
> 时间复杂度：$O(n)$

```java
import java.util.*;
public class Main {
    static Scanner s = new Scanner(System.in);
    public static void main(String[] args){
    	String num = s.next();
    	int n = num.length();   	
    	//特判 一位数
    	if(n == 1) {
    		int x = num.charAt(0) - '0';
    		if(x == 4 || x == 8) {
    			System.out.print(0);return;
    		}else {
    			System.out.print(-1);return;
    		}
    	}
    	// 0 次操作
    	int a = num.charAt(n - 2) - '0';
		int b = num.charAt(n - 1) - '0';
		if(isVlid(a, b)) {System.out.print(0);return;}
		// 1 ~ n - 1次操作
    	for(int i = 0; i<=n - 2; ++ i) {
     		a = num.charAt(i - 1 < 0 ? n - 1 : 0) - '0';//
    		b = num.charAt(i) - '0';
    		if(isVlid(a, b)) {
    			System.out.print(i + 1);return;
    		}
    	}
    	System.out.print(-1);
    }
    public static boolean isVlid(int a, int b) {
    	if(a % 2 == 0) {
			if(b == 4 || b == 8 || b == 0) {
				return true;
			}
		}else {
			if(b == 2 || b == 6) {
				return true;
			}
		}
    	return false;
    }
}
```

D. 小红的好串

[牛客 80742/D](https://ac.nowcoder.com/acm/contest/80742/D)

小红定义一个字符串是“好串”，当且仅当该该字符串在长度和它相等的字符串中，"red"子序列的数量是最多的。
 例如，"rreedd"是好串，因为包含了8个"red"子序列。而"redred"则不是好串。

 现在小红拿到了一个字符串，她有多次询问，每次询问一个区间，你需要回答将该区间对应的子串修改为好串的最小修改次数（每次修改可以修改任意一个字符）

> 用三个前缀和记录记录每个字母的出现情况，在比较时用前缀和计算。
>
> 对于好串的形式，应当让三个字母数量尽可能接近。当长度不是三的倍数时应当讨论三种情况。
>
> $O(n + m)$

![image-20240622112539834](images/image-20240622112539834.png)

```java
import java.io.*;
import java.util.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static int n, m, l , r, s[][];
    static char[] c;  
    public static void main(String[] args) throws Exception {
        n = sc.nextInt();
        m = sc.nextInt();
        c = sc.next().toCharArray();
        s = new int[n + 1][3];
        for(int i = 1; i <= n; i ++){
            s[i][getc(c[i - 1])] ++;
            for(int j = 0; j < 3; j ++) s[i][j] += s[i - 1][j];
        }
        while(m --> 0){
            l = sc.nextInt();
            r = sc.nextInt();
            int d = r - l + 1;
            if(d <= 2) {
                pw.println(0);
                continue;
            }
            int ans = (int) 1e9;
            int len = d / 3;
            if(d % 3 == 0){
                int k1 = l + len - 1, k2 = l + 2 * len - 1;
                ans = d - get(k1, k2); 
            }else if(d % 3 == 1){
                int k1 = l + len - 1, k2 = l + 2 * len - 1;
                ans = d - get(k1, k2);
                k2 ++;
                ans = Math.min(ans, d - get(k1, k2));
                k1 ++;
                ans = Math.min(ans, d - get(k1, k2));
            }else{
                int k1 = l + len, k2 = k1 + len + 1;
                ans = d - get(k1, k2);
                k2 --;
                ans = Math.min(ans, d - get(k1, k2));
                k1 --;
                ans = Math.min(ans, d - get(k1, k2));
            }
            pw.println(ans);
        }
        pw.flush();pw.close(); 
    }
    public static int get(int k1, int k2){
        return s[k1][0] - s[l - 1][0] + s[k2][1] - s[k1][1] + s[r][2] - s[k2][2];
    }
    public static int getc(char c){
        if(c == 'r') return 0;
        if(c == 'e') return 1;
        return 2;
    }
}

```

