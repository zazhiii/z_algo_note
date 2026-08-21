# 第 136 场双周赛（待补T4）

[3240. 最少翻转次数使二进制矩阵回文 II - 力扣（LeetCode）](https://leetcode.cn/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-ii/description/)

给你一个 `m x n` 的二进制矩阵 `grid` 。

如果矩阵中一行或者一列从前往后与从后往前读是一样的，那么我们称这一行或者这一列是 **回文** 的。

你可以将 `grid` 中任意格子的值 **翻转** ，也就是将格子里的值从 `0` 变成 `1` ，或者从 `1` 变成 `0` 。

请你返回 **最少** 翻转次数，使得矩阵中 **所有** 行和列都是 **回文的** ，且矩阵中 `1` 的数目可以被 `4` **整除** 。

> 思维

> 做思维题时，从最简单的情况开始思考。
>
> 1. 有四个镜像的地方一定满足1的个数是4的倍数，设四个位置有$c$个$1$操作数加$\min(c,4-c)$
> 2. 对于有中间一行或一列的格子，记录不需要改变的$1$的个数为$cnt$，需要操作的次数$diff$，$cnt\mod4$一定为2或0，若为0那么把$diff$操作的全变为0即可；若为2，那么从$diff$中拿一次出来变为1即可，若$diff$为0，就不能拿一次出来，就只能从$cnt$中将两个1变为0。
> 3. 对于有正中心的格子，这个格子一定要为$0$，不然1的总数一定为奇数，不可能为4的倍数

```java
class Solution {
    public int minFlips(int[][] a) {
        int n = a.length;
        int m = a[0].length;
        int ans = 0;
        for(int i = 0; i < n / 2; i ++){
            for(int j = 0; j < m / 2; j ++){
                int c = 0;
                c += a[i][j];
                c += a[i][m - 1 - j];
                c += a[n - 1 - i][j];
                c += a[n - 1 - i][m - 1 - j];
                ans += Math.min(c, 4 - c);
            }
        }
        int cnt = 0, diff = 0;
        if(n % 2 == 1){
            for(int j = 0; j < m / 2; j ++){
                if(a[n / 2][j] != a[n / 2][m - 1 - j]) diff ++;
                else cnt += a[n / 2][j] * 2;
            }
        }
        if(m % 2 == 1){
            for(int i = 0; i < n / 2; i ++){
                if(a[i][m / 2] != a[n - 1 - i][m / 2]) diff ++;
                else cnt += a[i][m / 2] * 2;
            }
        }
        if(n % 2 == 1 && m % 2 == 1) ans += a[n / 2][m / 2];
        
        if(diff > 0) ans += diff;
        else ans += cnt % 4;
        return ans;
    }
}
```

