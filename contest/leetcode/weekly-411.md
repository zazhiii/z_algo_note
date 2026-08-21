# 第 411 场周赛（待补T3）



[3260. 找出最大的 N 位 K 回文数 - 力扣（LeetCode）](https://leetcode.cn/problems/find-the-largest-palindrome-divisible-by-k/description/)



[3261. 统计满足 K 约束的子字符串数量 II](https://leetcode.cn/problems/count-substrings-that-satisfy-k-constraint-ii/)

给你一个 **二进制** 字符串 `s` 和一个整数 `k`。另给你一个二维整数数组 `queries` ，其中 `queries[i] = [li, ri]` 。

如果一个 **二进制字符串** 满足以下任一条件，则认为该字符串满足 **k 约束**：

- 字符串中 `0` 的数量最多为 `k`。
- 字符串中 `1` 的数量最多为 `k`。

返回一个整数数组 `answer` ，其中 `answer[i]` 表示 `s[li..ri]` 中满足 **k 约束** 的 子字符串 的数量。

> 前缀和、双指针、二分

> 枚举所有点`j`作为右端点，求出以该点为右端点的最长字串的左端点`i`，这一步用双指针实现：当因为右端点右移导致字串不合法时，移动左端点直到合法。用`left[]`记录每个右端点`j`的最远合法左端点`i`。
>
> 设询问区间`[l, r]`，其中一些点`j`的`left[j]`小于`l`，这些区间`[l, j]`中所有子串都合法，用公式求和字串数量$\frac{(len+1)\times len}{2}$；
>
> 对于某些点`k`的`left[k]`大于等于`l`，这些区间的字串用`k - left[k] + 1`计算一个点的合法子串数，对于所有这些点，用前缀和计算。
>
> 对于这两种点的分割点，用二分查找实现，因为`left[]`具有单调性，查找最右侧`left[i] < l`的点`i`即为第一种点的最右侧点

```java
class Solution {
    public long[] countKConstraintSubstrings(String s, int k, int[][] q) {
        char c[] = s.toCharArray();
        int n = c.length;
        // 记录以i为右端点的最长合法子串的左端点left[i]
        int left[] = new int[n];
        int t0 = 0, t1 = 0;
        for(int i = 0, j = 0; j < n; j ++){
            if(c[j] == '1') t1 ++;
            else t0 ++;
            while(t0 > k && t1 > k){
                if(c[i] == '1') t1 --;
                else t0 --;
                i ++;
            } 
            left[j] = i;
        }
        //前缀和
        long pre[] = new long[n + 1];
        for(int i = 0; i < n; i ++) pre[i + 1] = pre[i] + i - left[i] + 1;

        long ans[] = new long[q.length];
        for(int i = 0; i < q.length; i ++){
            //查找分界点
            int l = q[i][0], r = q[i][1], idx = q[i][0] - 1;
            while(l <= r){
                int m = (l + r) >>> 1;
                if(left[m] < q[i][0]) {idx = m; l = m + 1;}
                else r = m - 1;
            }
            // 公式计算前半段，前缀和计算后半段
            int len = idx - q[i][0] + 1;
            ans[i] += 1l * (len + 1) * len / 2;
            ans[i] += pre[q[i][1] + 1] - pre[idx + 1];
        }
        return ans;
    }
}
```

