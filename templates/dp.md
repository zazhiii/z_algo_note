# 动态规划模板

## 背包



### 01背包

[【模板】01背包 (nowcoder.com)](https://ac.nowcoder.com/acm/problem/226514)

你有一个背包，最多能容纳的体积是$V$。 

  现在有$n$个物品，第$i$个物品的体积为$v_i$ ,价值为$w_i$。 

  （1）求这个背包至多能装多大价值的物品？ 

  （2）若背包**恰好装满**，求至多能装多大价值的物品？

#### 二维dp数组

```java
import java.io.*;
import java.util.*;
public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(System.out);
    static int n, V, v[], w[], dp1[][], dp2[][];
    public static void main(String[] args) throws IOException {
        n = sc.nextInt();
        V = sc.nextInt();
        v = new int[n + 1];
        w = new int[n + 1];
        for(int i = 1; i <= n; i ++){
            v[i] = sc.nextInt();
            w[i] = sc.nextInt();
        }
        // dp1[i][j]: 在前i个物品中，容量为j的背包能装的最大价值
        dp1 = new int[n + 1][V + 1];
        // dp2[i][j]: 在前i个物品中，容量为j的背包能恰好装满的最大价值
        dp2 = new int[n + 1][V + 1];
        // 不能从0转移出去那些容量将会是-inf，即这些状态不可达
        for(int i = 0; i <= n; i ++){
            Arrays.fill(dp2[i], Integer.MIN_VALUE);
            dp2[i][0] = 0;
        }
        for(int i = 1; i <= n; i ++){
            for(int j = 1; j <= V; j ++){
                if(j < v[i]){
                    // 背包容量小于第i个物品的体积，只能不选。
                    dp1[i][j] = dp1[i - 1][j];
                    dp2[i][j] = dp2[i - 1][j];
                }else{
                    // 考虑: 选 | 不选
                    dp1[i][j] = Math.max(dp1[i - 1][j], dp1[i - 1][j - v[i]] + w[i]);
                    dp2[i][j] = dp2[i - 1][j];
                    if(dp2[i - 1][j - v[i]] != Integer.MIN_VALUE){
                        dp2[i][j] = Math.max(dp2[i][j], dp2[i - 1][j - v[i]] + w[i]);
                    }
                }
            }
        }
        pw.println(dp1[n][V]);
        pw.println(dp2[n][V] < 0 ? 0 : dp2[n][V]);
        pw.flush();
    }   
}
```

#### 一维dp数组

> 滚动数组将`dp`数组优化为一维

```java
import java.io.*;
import java.util.*;
public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(System.out);
    static int n, V, v[], w[], dp1[], dp2[];
    public static void main(String[] args) throws IOException {
        n = sc.nextInt();
        V = sc.nextInt();
        v = new int[n + 1];
        w = new int[n + 1];
        for(int i = 1; i <= n; i ++){
            v[i] = sc.nextInt();
            w[i] = sc.nextInt();
        }

        dp1 = new int[V + 1];
        dp2 = new int[V + 1];

        Arrays.fill(dp2, Integer.MIN_VALUE);
        dp2[0] = 0;

        for(int i = 1; i <= n; i ++){
            // 若选当前物品i，则需要容量j - v[i]在[1, i - 1]中能装的最大价值量加上w[i]。
            // 倒序遍历容量保证了当遍历到容量j时，dp[j - v[i]]还没有更新，
            // 他表示的就是容量j - v[i]在[1, i - 1]中能装的最大价值量。
            for(int j = V; j >= v[i]; j --){
                dp1[j] = Math.max(dp1[j], dp1[j - v[i]] + w[i]);
                if(dp2[j - v[i]] != Integer.MIN_VALUE){
                    dp2[j] = Math.max(dp2[j], dp2[j - v[i]] + w[i]);
                }
            }
        }
        pw.println(dp1[V]);
        pw.println(dp2[V] < 0 ? 0 : dp2[V]);
        pw.flush();
    }   
}
```

### 完全背包

[【模板】完全背包 (nowcoder.com)](https://ac.nowcoder.com/acm/problem/226516)

#### 二维dp数组

```java
import java.io.*;
import java.util.*;
public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(System.out);
    static int n, V, v[], w[], dp1[][], dp2[][];
    public static void main(String[] args) throws IOException {
        n = sc.nextInt();
        V = sc.nextInt();
        v = new int[n + 1];
        w = new int[n + 1];
        for(int i = 1; i <= n; i ++){
            v[i] = sc.nextInt();
            w[i] = sc.nextInt();
        }
        // dp1[i][j]: 在前i个物品中，容量为j的背包能装的最大价值
        dp1 = new int[n + 1][V + 1];
        // dp2[i][j]: 在前i个物品中，容量为j的背包能恰好装满的最大价值
        dp2 = new int[n + 1][V + 1];
        // 不能从0转移出去那些容量将会是-inf，即这些状态不可达
        for(int i = 0; i <= n; i ++){
            Arrays.fill(dp2[i], Integer.MIN_VALUE);
            dp2[i][0] = 0;
        }
        for(int i = 1; i <= n; i ++){
            for(int j = 1; j <= V; j ++){
                if(j < v[i]){
                    // 背包容量小于第i个物品的体积，只能不选。
                    dp1[i][j] = dp1[i - 1][j];
                    dp2[i][j] = dp2[i - 1][j];
                }else{
                    // 与01背包不同：
                    //     01背包选了当前物品，剩余的j - v[i]的容量只能从物品[1, i - 1]中选；
                    //     完全背包选了当前物品，剩余的j - v[i]的容量可以从物品[1, i]中选。
                    // 理解为 "选一个" 当前物品。
                    // 考虑: 不选 | 选一个
                    dp1[i][j] = Math.max(dp1[i - 1][j], dp1[i][j - v[i]] + w[i]);
                    dp2[i][j] = dp2[i - 1][j];
                    if(dp2[i][j - v[i]] != Integer.MIN_VALUE){
                        dp2[i][j] = Math.max(dp2[i][j], dp2[i][j - v[i]] + w[i]);
                    }
                }
            }
        }
        pw.println(dp1[n][V]);
        pw.println(dp2[n][V] < 0 ? 0 : dp2[n][V]);
        pw.flush();
    }   
}
```

#### 一维dp数组

```java
import java.io.*;
import java.util.*;
public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(System.out);
    static int n, V, v[], w[], dp1[], dp2[];
    public static void main(String[] args) throws IOException {
        n = sc.nextInt();
        V = sc.nextInt();
        v = new int[n + 1];
        w = new int[n + 1];
        for(int i = 1; i <= n; i ++){
            v[i] = sc.nextInt();
            w[i] = sc.nextInt();
        }

        dp1 = new int[V + 1];
        dp2 = new int[V + 1];

        Arrays.fill(dp2, Integer.MIN_VALUE);
        dp2[0] = 0;

        for(int i = 1; i <= n; i ++){
            // 选了当前物品后不是从[1, i - 1]中考虑，而是从[1, i]中考虑
            // 所以dp[j - v[i]]可以是更新过的。
            for(int j = v[i]; j <= V; j ++){
                dp1[j] = Math.max(dp1[j], dp1[j - v[i]] + w[i]);
                if(dp2[j - v[i]] != Integer.MIN_VALUE){
                    dp2[j] = Math.max(dp2[j], dp2[j - v[i]] + w[i]);
                }
            }
        }
        pw.println(dp1[V]);
        pw.println(dp2[V] < 0 ? 0 : dp2[V]);
        pw.flush();
    }   
}
```

### 多重背包

[多重背包 (nowcoder.com)](https://ac.nowcoder.com/acm/problem/235950)

有 $n$ 种物品，第 $i$ 种物品有 $x_i$ 个，每一个物品重量为 $w_i$ ，价值为 $v_i$ ，现有一个承重能力为 $T$ 的背包，在不超过承重能力的情况下，背包种最多能装多少价值的物品。

#### 二维dp数组

```java
import java.io.*;
import java.util.*;
public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(System.out);
    static int n, V, v[], w[], s[], dp[][];
    public static void main(String[] args) throws IOException {
        n = sc.nextInt();
        V = sc.nextInt();
        v = new int[n + 1];
        w = new int[n + 1];
        s = new int[n + 1];
        dp = new int[n + 1][V + 1];
        for(int i = 1; i <= n; i ++){
            v[i] = sc.nextInt();
            w[i] = sc.nextInt();
            s[i] = sc.nextInt();
        }
        for(int i = 1; i <= n; i ++){
            for(int j = 1; j <= V; j ++){
                // 第i种物品可以选择0 ~ K个
                // K不能超过该物品的数量 且 第i种物品总重量K * v[i]不超过当前背包容量 j
                for(int k = 0; k <= s[i] && k * v[i] <= j; k ++){
                    dp[i][j] = Math.max(dp[i][j], dp[i - 1][j - k * v[i]] + k * w[i]);
                }
            }
        }
        pw.println(dp[n][V]);
        pw.flush();
    }   
}
```

#### 一维dp数组

```java
import java.io.*;
import java.util.*;
public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(System.out);
    static int n, V, v[], w[], s[], dp[];
    public static void main(String[] args) throws IOException {
        n = sc.nextInt();
        V = sc.nextInt();
        v = new int[n + 1];
        w = new int[n + 1];
        s = new int[n + 1];
        dp = new int[V + 1];
        for(int i = 1; i <= n; i ++){
            v[i] = sc.nextInt();
            w[i] = sc.nextInt();
            s[i] = sc.nextInt();
        }
        for(int i = 1; i <= n; i ++){
            // 类似 01 背包，选了当前物品就只能从[1, i - 1]中考虑剩余容量能装最多多少价值了。
            // 倒序保证了遍历到j时，dp[j - v[i]]还没遍历到，还没更新，即表示的是从[1, i - 1]中考虑剩余容量能装最多多少价值
            for(int j = V; j >= v[i]; j --){
                for(int k = 0; k <= s[i] && k * v[i] <= j; k ++){
                    dp[j] = Math.max(dp[j], dp[j - k * v[i]] + k * w[i]);
                }
            }
        }
        pw.println(dp[V]);
        pw.flush();
    }   
}
```

#### 二进制优化

[5. 多重背包问题 II - AcWing题库](https://www.acwing.com/problem/content/5/)

```java
import java.io.*;
import java.util.*;
public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(System.out);
    static int n, V, v, w, s, dp[];
    public static void main(String[] args) throws IOException {
        n = sc.nextInt();
        V = sc.nextInt();
        dp = new int[V + 1];

        List<int[]> a = new ArrayList<>();
        for(int i = 1; i <= n; i ++){
            v = sc.nextInt();
            w = sc.nextInt();
            s = sc.nextInt();
            // 将s个物品拆成一系列2^k数量的物品，并将其看作一个物品
            for(int k = 1; k <= s; k *= 2){
                s -= k;
                a.add(new int[]{k * v, k * w});
            }
            // 拆完2^k数量剩余数量的物品单独作为一个物品。
            if(s > 0) a.add(new int[]{s * v, s * w});
        }
        // 问题转化为01背包
        for(int i = 0; i < a.size() ; i ++){
            for(int j = V; j >= a.get(i)[0]; j --){
                dp[j] = Math.max(dp[j], dp[j - a.get(i)[0]] + a.get(i)[1]);
            }
        }
        pw.println(dp[V]);
        pw.flush();
    }   
}
```

### 分组背包

```java
import java.io.*;
import java.util.*;
public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(System.out);
    static int n, V, v[][], w[][], s[], dp[];
    public static void main(String[] args) throws IOException {
        n = sc.nextInt();
        V = sc.nextInt();
        v = new int[n + 1][];
        w = new int[n + 1][];
        s = new int[n + 1];
        dp = new int[V + 1];
        for(int i = 1; i <= n; i ++){
            s[i] = sc.nextInt();
            v[i] = new int[s[i] + 1];
            w[i] = new int[s[i] + 1];
            for(int j = 1; j <= s[i]; j ++){
                v[i][j] = sc.nextInt();
                w[i][j] = sc.nextInt();
            }
        }

        for(int i = 1; i <= n; i ++){
            for(int j = V; j >= 1; j --){
                // 第i组的第k个物品
                for(int k = 1; k <= s[i]; k ++){
                    if(j >= v[i][k]) dp[j] = Math.max(dp[j], dp[j - v[i][k]] + w[i][k]);
                }
            }
        }
        pw.println(dp[V]);
        pw.flush();
    }   
}
```

## 经典线性dp

### 最大子串和

[P1115 最大子段和 - 洛谷 | 计算机科学教育新生态 (luogu.com.cn)](https://www.luogu.com.cn/problem/P1115)

```java
import java.io.*;
import java.util.*;
public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(System.out);
    static int n, a[], dp[];
    public static void main(String[] args) throws IOException {
        n = sc.nextInt();
        a = new int[n + 1];
        for(int i = 1; i <= n; i ++) a[i] = sc.nextInt();
        // dp[i]: 以第i个数结尾的最大子串和
        dp = new int[n + 1];
        int ans = -(int)1e9;
        for(int i = 1; i <= n; i ++){
            // 考虑: 从这个数重新开始计算 | 将这个数接到前一个和最大子串结尾
            dp[i] = Math.max(a[i], dp[i - 1] + a[i]);
            // 记录所有最大字串和的最大值
            ans = Math.max(ans, dp[i]);
        }
        pw.println(ans);
        pw.flush();
    }   
}
```



### 最长公共子序列`(LCS)`

### 最长递增子序列`(LIS)`
