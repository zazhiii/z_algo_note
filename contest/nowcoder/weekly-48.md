# 牛客周赛 Round 48

[B-小红的伪回文子串（easy）](https://ac.nowcoder.com/acm/contest/85187/B)

定义一个字符串的“伪回文值”是：修改最少字符数量使得其变成回文串的修改次数。例如，"abca"的伪回文值是1。任何回文串的伪回文值是0。

给定一个字符串，求出所有连续子串的伪回文值之和。(长度不超过100)

> 枚举|区间dp

> 法一：枚举所有字串，用双指针从两边判断需要修改多少个字符才能变为回文串。
>
> ​			$O(n^3)$
>
> 法二：$dp[i][j]$：表示$i\sim j$字串的伪回文值
>
> ​			若$a[i] = a[j], dp[i][j] = d[i + 1][j -1]$
>
> ​			否则，$dp[i][j] = dp[i+1][j -1] + 1$
>
> ​			枚举所有字串，求和得答案。
>
> ​			$O(n^2)$
>
> 法三：计算每一对字符对答案的贡献。
>
> ​			(从0开始)位置为$i，j$是多少个字串的对称位置呢？$min(i + 1, n - j)$个。
>
> ​			如果$a[i]\neq a[j] $，则该对字符对答案的贡献为$min(i + 1,n-j)$.
>
> ​			枚举所有字符对，求和贡献。
>
> ​			$O(n^2)$

```java
import java.io.*;
import java.util.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    public static void main(String[] args) throws Exception {
        char[] s = sc.next().toCharArray();
        int n = s.length;
        long ans = 0;
        for(int i = 0; i < n - 1; i ++){
            for(int j = i + 1; j < n; j ++){
                for(int l = i, r = j; l < r; l ++, r --){
                    if(s[l] != s[r]) ans ++;
                }
            }
        }
        pw.println(ans);
        pw.flush();pw.close(); 
    }
}
--------------------------------------------------------------------------------------
import java.io.*;
import java.util.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    public static void main(String[] args) throws Exception {
        char[] s = sc.next().toCharArray();
        int n = s.length;
        int dp[][] = new int[n + 1][n + 1];
        long ans = 0;
        for(int j = 2; j <= n ; j ++){
            for(int i = 1; i <= j - 1; i ++){// left:i right:j
                if(s[j - 1] == s[i - 1])  dp[i][j] = dp[i + 1][j - 1];
                else dp[i][j] = dp[i + 1][j - 1] + 1;
                ans += dp[i][j];
            }
        }
        pw.println(ans);
        pw.flush();pw.close(); 
    }
}
------------------------------------------------------------------------------
import java.io.*;
import java.util.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    public static void main(String[] args) throws Exception {
        char[] c = sc.next().toCharArray();
        int n = c.length;
        long ans = 0;
        for(int i = 0; i < n - 1; i ++){
            for(int j = i + 1; j < n; j ++){
                if(c[i] != c[j]) ans += Math.min(i + 1, n - j);
            }
        }
        pw.println(ans);
        pw.flush();pw.close(); 
    }
}
```

[E-小红的伪回文子串（hard）](https://ac.nowcoder.com/acm/contest/85187/E)

定义一个字符串的“伪回文值”是：修改最少字符数量使得其变成回文串的修改次数。例如，"abca"的伪回文值是1。任何回文串的伪回文值是0。

给定一个字符串，求出所有连续子串的伪回文值之和。(**长度不超过200000**)

> 由easy版的法三拓展。

```java
import java.io.*;
import java.util.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    public static void main(String[] args) throws Exception {
        char[] c = sc.next().toCharArray();
        int n = c.length;
        long cnt[][] = new long[n + 1][26];
        long sum[][] = new long[n + 1][26];
        long s[] = new long[n + 1];
        for(int i = 1; i <= n; i ++){
            s[i] = s[i - 1] + n - i + 1;
            cnt[i][c[i - 1] - 'a'] = 1;
            sum[i][c[i - 1] - 'a'] = n - i + 1;
            for(int j = 0; j < 26; j ++){
                cnt[i][j] += cnt[i - 1][j];
                sum[i][j] += sum[i - 1][j];
            }
        }
        long ans = 0;
        for(int i = 1; i <= n; i ++){
            int x = c[i - 1] - 'a';
            if(i <= n / 2){
                ans += (n - 2 * i - (cnt[n - i][x] - cnt[i][x])) * i;
                ans += s[n] - s[n - i] - (sum[n][x] - sum[n - i][x]);
            }else{
                ans += s[n] - s[i] - (sum[n][x] - sum[i][x]);
            }
        }
        pw.println(ans);
        pw.flush();pw.close(); 
    }
}
```

