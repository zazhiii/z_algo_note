# 第 398 场周赛

B. [100308. 特殊数组 II](https://leetcode.cn/contest/weekly-contest-398/problems/special-array-ii/)

如果数组的每一对相邻元素都是两个奇偶性不同的数字，则该数组被认为是一个 **特殊数组** 。

周洋哥有一个整数数组 `nums` 和一个二维整数矩阵 `queries`，对于 `queries[i] = [fromi, toi]`，请你帮助周洋哥检查子数组 `nums[fromi..toi]` 是不是一个 **特殊数组** 。

返回布尔数组 `answer`，如果 `nums[fromi..toi]` 是特殊数组，则 `answer[i]` 为 `true` ，否则，`answer[i]` 为 `false` 。

> tag：**前缀和**

> $st[i]$记录$0\sim i$有多少对不合法的数对。
>
> 对于每次询问的范围$l\sim r$，若中间没有不合法的数对则$st[r]=st[l]$，即特殊数组

```java
class Solution {
    public boolean[] isArraySpecial(int[] nums, int[][] queries) {
        int n = nums.length;
        int m = queries.length;
        boolean ans[] = new boolean[m];
        int s = 0;
        int st[] = new int[n];
        for(int i = 0; i < n - 1; i ++){
            if((nums[i] + nums[i + 1]) % 2 == 0) s ++;
            st[i + 1] = s;
        }
        for(int i = 0; i < m; i++){
            int l = queries[i][0];
            int r = queries[i][1];
            if(st[r] - st[l] > 0) ans[i] = true;
        }
        for(int i = 0; i < m; i++) ans[i] = !ans[i];
        return ans;
    }
}
```

