# [第 441 场周赛](https://leetcode.cn/contest/weekly-contest-441/)（exc: T4）

T2 [距离最小相等元素查询](https://leetcode.cn/problems/closest-equal-element-queries/)

> 环形数组处理，哈希表

```java
class Solution {
    public List<Integer> solveQueries(int[] nums, int[] q) {
        int n = nums.length;
        int[] a = new int[2 * n];
        // 环形数组处理成一个链
        for(int i = 0; i < nums.length; i ++){
            a[i] = a[i + n] = nums[i];
        }
        int[] map = new int[(int)1e6 + 1]; // map[x] 记录 x 上一次出现的索引
        Arrays.fill(map, -1);
        int[] dis = new int[n]; // 记录每个位置的数与他相同数的最近距离
        Arrays.fill(dis, (int)1e9);
        for(int i = 0; i < 2 * n; i ++){
            if(map[a[i]] != -1){// a[i] 出现过
                dis[i % n] = Math.min(dis[i % n], i - map[a[i]]); 
                //前一个位置的a[i]也要更新他的dis[preIdx]
                dis[map[a[i]] % n] = Math.min(dis[map[a[i]] % n], i - map[a[i]]);
            }
            map[a[i]] = i;
        }
        List<Integer> ans = new ArrayList<>();
        for(int x : q) ans.add(dis[x] < nums.length ? dis[x] : -1);
        return ans;
    }
}
```

T3 [3489. 零数组变换 IV - 力扣（LeetCode）](https://leetcode.cn/problems/zero-array-transformation-iv/description/)

> 01背包

```java
class Solution {
    public int minZeroArray(int[] a, int[][] qu) {
        int ans = 0;
        int[] t = new int[a.length];
        Arrays.fill(t, -1);
        for (int i = 0; i < a.length; i++) {
            if(a[i] == 0) t[i] = 0;
            // f[j][k]：前 j 个q的操作是否能凑出刚好为 k 的数
            boolean[][] f = new boolean[qu.length + 1][a[i] + 1];
            f[0][0] = true;
            for (int j = 1; j <= qu.length; j++) {
                int[] q = qu[j - 1];
                for (int k = 0; k <= a[i]; k++) {
                    // 在范围内 且 能操作
                    if (q[0] <= i && i <= q[1] && k >= q[2]) {
                        f[j][k] = f[j - 1][k - q[2]] || f[j - 1][k];
                    }else{
                        f[j][k] = f[j - 1][k];
                    }
                }
                if (f[j][a[i]] && t[i] == -1) {
                    t[i] = j;
                    ans = Math.max(t[i], ans);
                }
            }
            if (t[i] == -1)
                return -1;
        }
        return ans;
    }
}
```

