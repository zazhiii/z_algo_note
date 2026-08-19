# 贪心题单

[179. 最大数 - 力扣（LeetCode） ](https://leetcode.cn/problems/largest-number)  按两个数的拼接大小排序，`(b + a).compareTo(a + b)`

[1029. 两地调度 - 力扣（LeetCode）](https://leetcode.cn/problems/two-city-scheduling) 按差值排序

[线段重合_牛客题霸_牛客网](https://www.nowcoder.com/practice/1ae8d0b6bb4e4bcdbf64ec491f63fc37)  

> 1. 差分，因为首尾相连不算，所有区间左端点都右移一个位置，在这些地方+1，咋求最大即可 $O(n)$
> 2. 全部端点排序，端点需要标记一下是左右哪种端点，对于一个点，左端点数减去右端点数即重合区间数，因为首尾相连的不算重合，同一个点的所有右端点应该排到左端点前面，$O(n\log n)$
> 3. 小根堆，按左端点排序，遍历所有区间，对于一个区间，用堆记录大于当前区间的左端点的所有右端点（大于等于左端点的都弹出），堆中剩下的右端点数加上当前区间就是重叠数，记录最大即可。

[1353. 最多可以参加的会议数目 - 力扣（LeetCode）](https://leetcode.cn/problems/maximum-number-of-events-that-can-be-attended/)  

> 区间按左端点排序，遍历每一个点，对于当前点，考虑所有能在这个点开的会议，选择其中结束时间最早的会议在这个点开，用优先队列维护这些会议。

[502. IPO - 力扣（LeetCode）](https://leetcode.cn/problems/ipo) 每次在能够选取的项目中，选择利润最大的项目。用优先队列维护这些项目。

[581. 最短无序连续子数组 - 力扣（LeetCode）](https://leetcode.cn/problems/shortest-unsorted-continuous-subarray) 

>  找到最右侧的一个点，这个点的值没有大于其左侧所有值。同理找到左侧没有小于其右侧所有值的点，计算两点差值，若大于0则为答案，否则数组长度为答案



## 反悔贪心

[630. 课程表 III - 力扣（LeetCode）](https://leetcode.cn/problems/course-schedule-iii)  

## huffman编码

[P1090  合并果子  - 洛谷 ](https://www.luogu.com.cn/problem/P1090) 



---

[871. 最低加油次数 - 力扣（LeetCode）](https://leetcode.cn/problems/minimum-number-of-refueling-stops) [贪心、优先队列]  

[LCR 132. 砍竹子 II - 力扣（LeetCode）](https://leetcode.cn/problems/jian-sheng-zi-ii-lcof) 找规律、结论

将数字$n$分为$k$份，使得乘积尽量大。$n,k\le10^{12}$  拆成每一份尽量接近

```java
    public static int check2(int n, int k){
        if(k == 1) return n;
        return check2(n - n / k, k - 1) * (n / k);
    }
```



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
