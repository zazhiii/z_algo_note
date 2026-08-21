# 第 415 场周赛（exc：T3，T4  AC自动机）

T2 [3290. 最高乘法得分](https://leetcode.cn/problems/maximum-multiplication-score/)

给你一个大小为 4 的整数数组 `a` 和一个大小 **至少**为 4 的整数数组 `b`。

你需要从数组 `b` 中选择四个下标 `i0`, `i1`, `i2`, 和 `i3`，并满足 `i0 < i1 < i2 < i3`。你的得分将是 `a[0] * b[i0] + a[1] * b[i1] + a[2] * b[i2] + a[3] * b[i3]` 的值。

返回你能够获得的 **最大** 得分。

> dp
>
> `dp[i][j]`：用`a`的前`j`个数和`b`的前`i`个数中的`j`个数相乘能得到的最大得分
>
> 转移：`dp[i][j] = max(dp[i - 1][j - 1] + a[j - 1] * b[i - 1], dp[i - 1][j])`（是否用`b`的第`i`个数与`a`的第`j`个数相乘）
>
> 注意：初始化`dp`数组不要用`Long.MIN_VALE`因为他再加上一个负数会爆Long

```java
class Solution {
    public long maxScore(int[] a, int[] b) {
        int n = b.length;
        long dp[][] = new long[n + 1][5];
        Arrays.fill(dp[0], Long.MIN_VALUE / 2);
        dp[0][0] = 0;
        long ans = Long.MIN_VALUE / 2;
        for(int i = 1; i <= n; i ++){
            for(int j = 1; j <= 4; j ++){
                dp[i][j] = Math.max(dp[i - 1][j - 1] + 1L * a[j - 1] * b[i - 1], dp[i - 1][j]);
            }
        }
        return dp[n][4];
    }   
}
```

[3292. 形成目标字符串需要的最少字符串数 II - 力扣（LeetCode）](https://leetcode.cn/problems/minimum-number-of-valid-strings-to-form-target-ii/description/)

给你一个字符串数组 `words` 和一个字符串 `target`。如果字符串 `x` 是 `words` 中 **任意** 字符串的前缀，则认为 `x` 是一个 **有效** 字符串。现计划通过 **连接** 有效字符串形成 `target` ，返回需要连接的 **最少** 字符串数量。如果无法通过这种方式形成 `target`，则返回 `-1`。

