# 第 399 场周赛（exc：T4线段树）

C. [3164. 优质数对的总数 II](https://leetcode.cn/problems/find-the-number-of-good-pairs-ii/)

给你两个整数数组 `nums1` 和 `nums2`，长度分别为 `n` 和 `m`。同时给你一个**正整数** `k`。

如果 `nums1[i]` 可以被 `nums2[j] * k` 整除，则称数对 `(i, j)` 为 **优质数对**（`0 <= i <= n - 1`, `0 <= j <= m - 1`）。

返回 **优质数对** 的总数。

>    **若$a \mod b=0$则$b$一定是$a$的一个因子。**
>
>    枚举$nums_1$中所有数的因子以及每个因子的数量（即有多少个$nums[i]$包含这个因子）。
>
>    枚举$nums_2[i]\times k$判断是否在上述因子集合中，若在答案数累加上因子数
>
>    $O(n\times \sqrt{10^6} + m)$

```java
class Solution {
    int maxn = (int)1e6;
    int f[] = new int[maxn + 1];
    public long numberOfPairs(int[] a, int[] b, int k) {
        for(int i = 0; i < a.length; i ++){
            if(a[i] % k != 0) continue;
            int x = a[i] / k;
            for(int d = 1; d * d <= x; d ++){
                if(x % d != 0) continue;
                f[d] ++;
                if(d * d < x) f[x / d] ++;
            }
        }
        long ans = 0;
        for(int i = 0; i < b.length; i ++) ans += f[b[i]];
        return ans;
    }
}
```

> 枚举倍数
>
> `a[i]`被`b[i] * k`整除，枚举`b[i] * k`的所有倍数，记录**每个倍数**是多少个`b[i] * k`的倍数，遍历`a`累加`a[i]`是多少个`b[i] * k`的倍数。枚举倍数的上限为`a[i]`中的最大值，且相同的`b[i]`不用重复枚举，他们的倍数都是一致的。

```java
class Solution {
    int maxn = (int)1e6;
    int f[] = new int[maxn + 1];
    public long numberOfPairs(int[] a, int[] b, int k) {
        int max1 = 0;
        for(int x : a) max1 = Math.max(max1, x);
        // 记录b中每种数有多少个
        Map<Integer, Integer> map = new HashMap<>();
        for(int x : b) map.put(x, map.getOrDefault(x, 0) + 1);
        // 不用枚举所有b[i], 对于相同的b[i]其倍数一样，枚举一次就行
        for(int bi : map.keySet()){
            for(int j = bi * k; j <= max1; j += bi * k){
                f[j] += map.get(bi);
            }
        }
        long ans = 0;
        for(int i = 0; i < a.length; i ++) ans += f[a[i]];
        return ans;
    }
}
```

