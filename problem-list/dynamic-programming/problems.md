# 动态规划题单

## 一. 动态规划入门

> 一些简单的动态规划问题，感受一下「递推」

[509. 斐波那契数](https://leetcode.cn/problems/fibonacci-number/)

[70. 爬楼梯](https://leetcode.cn/problems/climbing-stairs/)

[746. 使用最小花费爬楼梯](https://leetcode.cn/problems/min-cost-climbing-stairs/)

[P1216 [USACO1.5\] [IOI1994]数字三角形 Number Triangles - 洛谷 | 计算机科学教育新生态 (luogu.com.cn)](https://www.luogu.com.cn/problem/P1216)

> 从小范围开始，寻找规律，得到递推式

[790. 多米诺和托米诺平铺 - 力扣（LeetCode）](https://leetcode.cn/problems/domino-and-tromino-tiling) 

[P1990 覆盖墙壁 - 洛谷](https://www.luogu.com.cn/problem/P1990)

## 二. 背包

### 2.1 `01`背包

> 「选」或者「不选」

[01背包](https://ac.nowcoder.com/acm/problem/226514) 【模板】

[P1048 [NOIP2005 普及组] 采药 - 洛谷 | 计算机科学教育新生态 (luogu.com.cn)](https://www.luogu.com.cn/problem/P1048) 【模板】

---

[P1049 [NOIP2001 普及组] 装箱问题 - 洛谷 | 计算机科学教育新生态 (luogu.com.cn)](https://www.luogu.com.cn/problem/P1049) 橙

[P1060 [NOIP 2006 普及组] 开心的金明 - 洛谷](https://www.luogu.com.cn/problem/P1060) 橙

[P1802 5 倍经验日 - 洛谷 | 计算机科学教育新生态 (luogu.com.cn) ](https://www.luogu.com.cn/problem/P1802) 橙

[P1507 NASA的食物计划 - 洛谷](https://www.luogu.com.cn/problem/P1507) 橙

[P1855 榨取kkksc03 - 洛谷](https://www.luogu.com.cn/problem/P1855) 橙

[2915. 和为目标值的最长子序列的长度 - 力扣（LeetCode）](https://leetcode.cn/problems/length-of-the-longest-subsequence-that-sums-to-target) 1659



**分割等和子串**

> 问题： 将一个集合分为两个最接近的子集。
>
> 设集合总和为`S`，用一个容量为`S/2`的背包去装集合里的元素，求得能装的最大值`dp[S/2]`则为小于`S/2`且最接近`S/2`的子集，`S-dp[S/2]`则为较大者子集；

[416. 分割等和子集 - 力扣（LeetCode）](https://leetcode.cn/problems/partition-equal-subset-sum) 

[1049. 最后一块石头的重量 II](https://leetcode.cn/problems/last-stone-weight-ii/)

[P2392 kkksc03考前临时抱佛脚 - 洛谷](https://www.luogu.com.cn/problem/P2392) 橙



### 2.2 完全背包

[完全背包](https://ac.nowcoder.com/acm/problem/226516) 【模板】

[P1616 疯狂的采药 - 洛谷 | 计算机科学教育新生态 (luogu.com.cn)](https://www.luogu.com.cn/problem/P1616)



### 2.3 多重背包

[P1833 樱花 - 洛谷](https://www.luogu.com.cn/problem/P1833) [二进制优化多重背包模板题] 

[P5020 [NOIP 2018 提高组] 货币系统 - 洛谷](https://www.luogu.com.cn/problem/P5020)  绿



## 三. 经典问题

### 经典问题

**子序列问题**

[牛客 226831](https://ac.nowcoder.com/acm/problem/226831)「最长递增子序列 `LIS`」

**最长公共子序列**

>    若$A_i=B_i$，$dp[i][j] = dp[i-1][j-1]+1$。
>
>    否则，$dp[i][j] = max(dp[i-1][j],dp[i][j-1])$

**编辑距离**

[洛谷 P2758](https://www.luogu.com.cn/problem/P2758) 「编辑距离」

**最大子数组和**

https://leetcode.cn/problems/maximum-subarray/description/ template
https://www.luogu.com.cn/problem/P1115 template

https://leetcode.cn/problems/maximum-pulse-value-after-one-subarray-rotation/description/



## 四. 线性`dp`

[洛谷 P2679](https://www.luogu.com.cn/problem/P2679)

[洛谷 P2340](https://www.luogu.com.cn/problem/P2340)

[洛谷 P1854](https://www.luogu.com.cn/problem/P1854)

[洛谷 P1044](https://www.luogu.com.cn/problem/P1044)  dp | 记忆化搜索

[洛谷 P1113](https://www.luogu.com.cn/problem/P1113) 黄；不止一种方法。

[洛谷 P1002](https://www.luogu.com.cn/problem/P1002) 橙

[洛谷 P2285](https://www.luogu.com.cn/problem/P2285) 黄

[洛谷 P3842](https://www.luogu.com.cn/problem/P3842)

[洛谷 P2196](https://www.luogu.com.cn/problem/P2196)

[洛谷 P1359](https://www.luogu.com.cn/problem/P1359)

[洛谷 P1020](https://www.luogu.com.cn/problem/P1020)

[洛谷 P1091](https://www.luogu.com.cn/problem/P1091)

[洛谷 P1541](https://www.luogu.com.cn/problem/P1541)

[洛谷 P1868](https://www.luogu.com.cn/problem/P1868)

[洛谷 P1725](https://www.luogu.com.cn/problem/P1725)

[洛谷 P1435](https://www.luogu.com.cn/problem/P1435)

[洛谷 P4933](https://www.luogu.com.cn/problem/P4933)

[洛谷 P1874](https://www.luogu.com.cn/problem/P1874)

[洛谷 P1164](https://www.luogu.com.cn/problem/P1164)

[洛谷 P1077](https://www.luogu.com.cn/problem/P1077)



[LeetCode egg-drop-with-2-eggs-and-n-floors](https://leetcode.cn/problems/egg-drop-with-2-eggs-and-n-floors)

[LeetCode count-number-of-texts](https://leetcode.cn/problems/count-number-of-texts)	1857； 计数 线性dp

[LeetCode minimum-white-tiles-after-covering-with-carpets](https://leetcode.cn/problems/minimum-white-tiles-after-covering-with-carpets) 2106

[LeetCode palindrome-partitioning-ii](https://leetcode.cn/problems/palindrome-partitioning-ii)	困难

[LeetCode unique-paths-ii](https://leetcode.cn/problems/unique-paths-ii/)

[LeetCode solving-questions-with-brainpower](https://leetcode.cn/problems/solving-questions-with-brainpower)	1709

[LeetCode coin-change-ii](https://leetcode.cn/problems/coin-change-ii)

[LeetCode combination-sum-iv](https://leetcode.cn/problems/combination-sum-iv)

[LeetCode coin-change](https://leetcode.cn/problems/coin-change/)

[LeetCode perfect-squares](https://leetcode.cn/problems/perfect-squares/)

[LeetCode total-characters-in-string-after-transformations-i](https://leetcode.cn/problems/total-characters-in-string-after-transformations-i)	1806

[LeetCode find-the-maximum-sum-of-node-values](https://leetcode.cn/problems/find-the-maximum-sum-of-node-values)	2268；思考树上操作有什么性质？

[LeetCode count-partitions-with-max-min-difference-at-most-k](https://leetcode.cn/problems/count-partitions-with-max-min-difference-at-most-k/) 单调队列优化 dp


使得数组非严格递增最小操作数
https://codeforces.com/contest/713/problem/C O(n^2)数据
https://www.luogu.com.cn/problem/P4597 O(nlog n)数据

## 五. 区间dp

[P1775 石子合并（弱化版） - 洛谷](https://www.luogu.com.cn/problem/P1775) 黄

[3472. 至多 K 次操作后的最长回文子序列 - 力扣（LeetCode）](https://leetcode.cn/problems/longest-palindromic-subsequence-after-at-most-k-operations) 1884

[D-智乃与长短期主义者博弈_牛客小白月赛110](https://ac.nowcoder.com/acm/contest/101918/D) 

[LeetCode minimum-score-triangulation-of-polygon](https://leetcode.cn/problems/minimum-score-triangulation-of-polygon/)	2130；区间dp + 枚举 + 记忆化搜索

[LeetCode stone-game-v](https://leetcode.cn/problems/stone-game-v/description) 2087；区间dp、枚举

## 六. 记忆化搜索

[P1434 SHOI2002\] 滑雪 - 洛谷](https://www.luogu.com.cn/problem/P1434) 黄

[P4017 最大食物链计数 - 洛谷](https://www.luogu.com.cn/problem/P4017) 记忆化搜索 | 拓扑排序

[1387. 将整数按权重排序 - 力扣（LeetCode）](https://leetcode.cn/problems/sort-integers-by-the-power-value) 1507

[3040. 相同分数的最大操作数目 II](https://leetcode.cn/problems/maximum-number-of-operations-with-the-same-score-ii/)

[LeetCode largest-color-value-in-a-directed-graph](https://leetcode.cn/problems/largest-color-value-in-a-directed-graph)    有向图中判环；


## 七. 树型dp

[C-Cidoai的树上方案_牛客练习赛128 (nowcoder.com)](https://ac.nowcoder.com/acm/contest/88880/C)



## 八. 期望/概率dp

[F-口吃_牛客周赛 Round 60](https://ac.nowcoder.com/acm/contest/90070/F)

[F-小红的小球染色期望_牛客周赛 Round 79](https://ac.nowcoder.com/acm/contest/100902/F) 



## 九. 数位dp

[2843. 统计对称整数的数目 - 力扣（LeetCode）](https://leetcode.cn/problems/count-symmetric-integers) 1270；枚举 || 数位dp

[902. 最大为 N 的数字组合 - 力扣（LeetCode）](https://leetcode.cn/problems/numbers-at-most-n-given-digit-set) 1990

[2376. 统计特殊整数 - 力扣（LeetCode）](https://leetcode.cn/problems/count-special-integers) 2120

[1012. 至少有 1 位重复的数字 - 力扣（LeetCode）](https://leetcode.cn/problems/numbers-with-repeated-digits) 2230

[2999. 统计强大整数的数目 - 力扣（LeetCode）](https://leetcode.cn/problems/count-the-number-of-powerful-integers) 2351；**TODO**

[2719. 统计整数数目 - 力扣（LeetCode）](https://leetcode.cn/problems/count-of-integers) 2355

[600. 不含连续1的非负整数 - 力扣（LeetCode）](https://leetcode.cn/problems/non-negative-integers-without-consecutive-ones) 二进制位的数位dp



[P2657 [SCOI2009] windy 数 - 洛谷](https://www.luogu.com.cn/problem/P2657) 蓝

[P3413 SAC#1 - 萌数 - 洛谷](https://www.luogu.com.cn/problem/P3413) 紫；**正难则反**



[C - Snake Numbers](https://atcoder.jp/contests/abc387/tasks/abc387_c) 1249





