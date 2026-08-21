# 第 402 场周赛

[3185. 构成整天的下标对数目 II](https://leetcode.cn/problems/count-pairs-that-form-a-complete-day-ii/)

给你一个整数数组 `hours`，表示以 **小时** 为单位的时间，返回一个整数，表示满足 `i < j` 且 `hours[i] + hours[j]` 构成 **整天** 的下标对 `i`, `j` 的数目。

**整天** 定义为时间持续时间是 24 小时的 **整数倍** 。

例如，1 天是 24 小时，2 天是 48 小时，3 天是 72 小时，以此类推。

> 类似两数之和的哈希表做法。
>
> 另外若$(a+b) \mod 24 = 0 $且$a、b$不是24的倍数的话、$a\mod 24+b\mod 24=24$。
>
> 先将所有元素$\mod 24$
>
> 单独统计24的倍数`cnt`。再统计$a+b=24$的对数（两数之和）
>
> 其中哈希表可以用一个长度$24$的数组优化。

```java
class Solution {
    public long countCompleteDayPairs(int[] a) {
        long ans = 0, n = a.length, cnt = 0;
        Map<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < n; i ++) {
            a[i] %= 24;
            if(a[i] == 0) cnt ++;
            else{
                ans += map.getOrDefault(24 - a[i], 0);
                map.put(a[i], map.getOrDefault(a[i], 0) + 1);
            }
        }
        ans += (cnt - 1) * cnt / 2;
        return ans;
    }
}
```

[3186. 施咒的最大总伤害](https://leetcode.cn/problems/maximum-total-damage-with-spell-casting/)

给你一个数组 `power` ，其中每个元素表示一个咒语的伤害值，可能会有多个咒语有相同的伤害值。

已知魔法师使用伤害值为 `power[i]` 的咒语时，他们就 **不能** 使用伤害为 `power[i] - 2` ，`power[i] - 1` ，`power[i] + 1` 或者 `power[i] + 2` 的咒语。

每个咒语最多只能被使用 **一次** 。

请你返回这个魔法师可以达到的伤害值之和的 **最大值** 

> 状态机dp

> 法一：双指针、哈希表、dp
>
> 将咒语大小和数量存入哈希表，将键取出排序。
>
> $dp[i]$：表示在$0\sim i$个数中能取到的最大值。
>
> $dp[i] =max(dp[i-1],dp[j]+a[i]*(number\ of\ a[i])$，其中$j$表示小于$a[i]-2$的最大数的下标。
>
> 对于$i$增加$j$单调不减，所以用一个指针寻找$j$
>
> 排序 ： $O(n\log n)$ 双指针：$O(n)$

```java
class Solution {
    public long maximumTotalDamage(int[] p) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int x : p) map.put(x, map.getOrDefault(x, 0) + 1);
        int n = map.size();
        int a[] = new int[n], k = 0;
        for(int x : map.keySet()) a[k ++] = x;
        Arrays.sort(a);
        long dp[] = new long[n + 1];
        for(int i = 0, j = 0; i < n; i ++){
            while(a[j] < a[i] - 2) j ++;
            dp[i + 1] = Math.max(dp[i], dp[j] + 1l * a[i] * map.get(a[i]));
        }
        return dp[n];
    }
}
```

> 法二：排序、二分查找、dp
>
> $dp[i][1/0]$：选/不选第$i$个数$0\sim i$能取到的最大值。
>
> 从左往右遍历，分情况讨论$i$和$i -1$的关系，写对应的转移方程。（见代码）
>
> $O(n\log n)$

```java
class Solution {
    public long maximumTotalDamage(int[] p) {
        int n = p.length, a[] = new int[n + 1], k = 1;
        for(int x : p) a[k ++] = x;
        Arrays.sort(a);
        long dp[][] = new long[n + 1][2];
        for(int i = 1; i <= n; i ++){
            if(a[i] - a[i - 1] > 2){
                dp[i][0] = Math.max(dp[i - 1][0], dp[i - 1][1]);
                dp[i][1] = dp[i][0] + a[i];
            }else if(a[i] == a[i - 1]){
                dp[i][0] = dp[i - 1][0];
                dp[i][1] = dp[i - 1][1] + a[i];
            }else{
                int l = 0, r = i - 1, idx = 0;
                while(l <= r){
                    int m = (l + r) >> 1;
                    if(a[m] < a[i] - 2){
                        idx = m;
                        l = m + 1;
                    }else{
                        r = m - 1;
                    }
                }
                dp[i][0] = Math.max(dp[i - 1][0], dp[i - 1][1]);
                dp[i][1] = Math.max(dp[idx][0], dp[idx][1]) + a[i];
            }
        }            
        return Math.max(dp[n][0], dp[n][1]);
    }
}
```

