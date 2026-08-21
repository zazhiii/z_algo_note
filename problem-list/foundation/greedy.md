# 贪心题单

[179. 最大数 - 力扣（LeetCode） ](https://leetcode.cn/problems/largest-number)  按两个数的拼接大小排序，`(b + a).compareTo(a + b)`

[1029. 两地调度 - 力扣（LeetCode）](https://leetcode.cn/problems/two-city-scheduling) 按差值排序

[线段重合_牛客题霸_牛客网](https://www.nowcoder.com/practice/1ae8d0b6bb4e4bcdbf64ec491f63fc37) 差分、端点排序或小根堆；注意端点相接不算重合。

[1353. 最多可以参加的会议数目 - 力扣（LeetCode）](https://leetcode.cn/problems/maximum-number-of-events-that-can-be-attended/) 按开始时间扫描，用小根堆选择最早结束的可参加会议。

[502. IPO - 力扣（LeetCode）](https://leetcode.cn/problems/ipo) 每次在能够选取的项目中，选择利润最大的项目。用优先队列维护这些项目。

[581. 最短无序连续子数组 - 力扣（LeetCode）](https://leetcode.cn/problems/shortest-unsorted-continuous-subarray) 用前缀最大值和后缀最小值确定边界。

## 反悔贪心

[630. 课程表 III - 力扣（LeetCode）](https://leetcode.cn/problems/course-schedule-iii)  

## huffman编码

[P1090  合并果子  - 洛谷 ](https://www.luogu.com.cn/problem/P1090) 



---

[871. 最低加油次数 - 力扣（LeetCode）](https://leetcode.cn/problems/minimum-number-of-refueling-stops) [贪心、优先队列]  

[LCR 132. 砍竹子 II - 力扣（LeetCode）](https://leetcode.cn/problems/jian-sheng-zi-ii-lcof) 找规律、结论

通用策略、复杂度与迁移出的详细笔记见 [贪心模板](../../templates/foundation/greedy.md)。

## 区间贪心

### 区间选点

[452. 用最少数量的箭引爆气球](https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/)【经典问题】

### 不相交区间

[646. 最长数对链](https://leetcode.cn/problems/maximum-length-of-pair-chain/)【经典问题】

[435. 无重叠区间](https://leetcode.cn/problems/non-overlapping-intervals/)

[D. Kousuke's Assignment](https://codeforces.com/contest/2033/problem/D)

### 区间分组

[LeetCode divide-intervals-into-minimum-number-of-groups](https://leetcode.cn/problems/divide-intervals-into-minimum-number-of-groups)【经典问题】

### 区间覆盖

[LeetCode jump-game-ii](https://leetcode.cn/problems/jump-game-ii/)

[LeetCode video-stitching](https://leetcode.cn/problems/video-stitching/) 可转化为：45.跳跃游戏

[LeetCode minimum-number-of-taps-to-open-to-water-a-garden](https://leetcode.cn/problems/minimum-number-of-taps-to-open-to-water-a-garden)可转化为：45.跳跃游戏

---

[LeetCode break-a-palindrome](https://leetcode.cn/problems/break-a-palindrome/)	1474

[LeetCode maximum-number-of-eaten-apples](https://leetcode.cn/problems/maximum-number-of-eaten-apples)  1930

[LeetCode zero-array-transformation-iii](https://leetcode.cn/problems/zero-array-transformation-iii)	2424；贪心、最大堆、差分；
