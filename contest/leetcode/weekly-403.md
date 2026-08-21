# LeetCode 第 403 场周赛

## 100337. 最大化子数组的总成本

### 基本信息

| 字段 | 内容 |
| --- | --- |
| 平台 | LeetCode |
| 题号 | 100337（周赛 T3） |
| 原题链接 | [最大化子数组的总成本](https://leetcode.cn/problems/maximize-total-cost-of-alternating-subarrays/) |
| 难度 / Rating | TODO |
| 知识点标签 | 动态规划 |

### 题意概括

给定长度为 `n` 的整数数组 `nums`。子数组 `nums[l..r]` 的成本定义为：

```
cost(l, r) = nums[l] - nums[l + 1] + ... + nums[r] * (−1)^(r − l)
```

将 `nums` 分割成若干子数组，使所有子数组的成本之和最大，并确保每个元素恰好属于一个子数组。返回最优分割方式下的最大总成本。

### 核心思路

定义 `dp[i][0/1]` 表示第 $i$ 个数取正号或负号时，前 $0\sim i$ 个数能够得到的最大成本。原代码记录的转移为：

```text
dp[i][0] = max(dp[i - 1][0], dp[i - 1][1]) + a[i]
dp[i][1] = dp[i - 1][0] - a[i]
```

### 正确性说明

TODO：原文未提供正确性说明。

### 复杂度

- 时间复杂度：TODO
- 空间复杂度：TODO

### 易错点

- TODO：原文未记录易错点。

### 代码

#### Java

```java
class Solution {
    /*  dp[i][0/1]: 第i个数取正/负0~i最大成本
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1]) + a[i]
        dp[i][1] = dp[i - 1][0] - a[i]
     */
    public long maximumTotalCost(int[] a) {
        long ans = 0;
        int n = a.length;
        long dp[][] = new long[n + 1][2];
        dp[1][0] = a[0];
        dp[1][1] = a[0];
        for(int i = 2; i <= n; i ++){
            dp[i][0] = Math.max(dp[i - 1][0], dp[i - 1][1]) + a[i - 1];
            dp[i][1] = dp[i - 1][0] - a[i - 1];
        }
        return Math.max(dp[n][0], dp[n][1]);
    }
}
```

#### Python

TODO：原文未提供 Python 代码。

### 复盘与可迁移结论

- TODO：原文未记录复盘或可迁移结论。
