# [Codeforces Round 958 (Div. 2)](https://codeforces.com/contest/1988)

## C - TODO：题目名称

### 基本信息

| 字段 | 内容 |
| --- | --- |
| 平台 | Codeforces |
| 题号 | 1988C |
| 原题链接 | [Problem C](https://codeforces.com/contest/1988/problem/C) |
| 难度 / Rating | TODO |
| 知识点标签 | 位运算、lowbit |

### 题意概括

给定正整数 $n$，构造最长序列 $a=[a_1,a_2,\ldots,a_k]$，满足：

- 对所有 $1\le i\le k$，$a_i\le n$；
- $a$ 严格递增；
- 对所有 $2\le i\le k$，$a_i\,|\,a_{i-1}=n$，其中 $|$ 代表按位或。

### 核心思路

要使序列最长，从最大数开始构造，最大值一定是 $n$ 本身，次大值为 $n-lowbit(n)$，依次类推，可以构造出长度为 $bitcount(n)+1$ 的序列。

### 正确性说明

TODO：原文未提供完整的正确性说明。

### 复杂度

- 时间复杂度：原文记录为 $O(n+n\log n)$，瓶颈在排序；TODO：待复核。
- 空间复杂度：TODO

### 易错点

- 构造目标是最长且严格递增，原文采用从最大值反向构造、最后排序的方式。

### 代码

#### Java

```java
import java.io.*;
import java.util.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    public static void solve(){
        long n = sc.nextLong();
        Vector<Long> ans = new Vector<>();
        long x = n;
        while(x > 0){
            long e = n - (x & -x);
            if(e != 0) ans.add(e);
            x -= (x & -x);
        }
        ans.add(n);
        Collections.sort(ans);
        pw.println(ans.size());
        for(long e : ans) pw.print(e + " ");
        pw.println();
    }
    public static void main(String[] args) throws IOException {
        int T = sc.nextInt();
        while(T --> 0){solve();}
        pw.flush();pw.close();
    }
}
```

#### Python

TODO：原文未提供 Python 代码。

### 复盘与可迁移结论

- TODO：原文未记录复盘或可迁移结论。
