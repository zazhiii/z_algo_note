# 第 397 场周赛

[100296. 两个字符串的排列差](https://leetcode.cn/problems/permutation-difference-between-two-strings/)

给你两个字符串 `s` 和 `t`，每个字符串中的字符都不重复，且 `t` 是 `s` 的一个排列。

**排列差** 定义为 `s` 和 `t` 中每个字符在两个字符串中位置的绝对差值之和。

返回 `s` 和 `t` 之间的 **排列差** 。

>    哈希表存储`s`的字母的位置，询问`t`字母找出在s中的位置和当前位置求绝对值，累加

```java
class Solution {
	    Map<Character, Integer> map = new HashMap<>();
	    public int findPermutationDifference(String s, String t) {
            int n = s.length();
	        for(int i = 0; i<=n -1; i++){
	            map.put(s.charAt(i), i);//存 字母--位置
	        }
	        int ans = 0;
	        for(int i = 0; i<=s.length() - 1; i++){
	            ans += Math.abs(map.get(t.charAt(i)) - i);//计算位置
	        }
			return ans;
	    }
	}
```

B[100274. 从魔法师身上吸取的最大能量](https://leetcode.cn/problems/taking-maximum-energy-from-the-mystic-dungeon/)

在神秘的地牢中，`n` 个魔法师站成一排。每个魔法师都拥有一个属性，这个属性可以给你提供能量。有些魔法师可能会给你负能量，即从你身上吸取能量。

你被施加了一种诅咒，当你从魔法师 `i` 处吸收能量后，你将被立即传送到魔法师 `(i + k)` 处。这一过程将重复进行，直到你到达一个不存在 `(i + k)` 的魔法师为止。

换句话说，你将选择一个起点，然后以 `k` 为间隔跳跃，直到到达魔法师序列的末端，**在过程中吸收所有的能量**。

给定一个数组 `energy` 和一个整数`k`，返回你能获得的 **最大** 能量。

>    第$i$个位置由第$i-k$跳过来。
>
>    $dp[i] = dp[i-k]+energy[i]$
>
>    $ans = max(dp[j]),(j\in[n-k,n-1])$

```java
	class Solution {
	    public int maximumEnergy(int[] energy, int k) {
            int e[] = energy.clone();
            int n = energy.length;
			int[] dp = new int[n];
	    	for(int i= 0; i<=n - 1; i ++) dp[i] = e[i];
            int ans = -(int)1e9;
	    	for(int i = k; i<= n - 1; i++) {
	    		dp[i] = Math.max(dp[i - k] + energy[i], e[i]);
	    	}
            for(int i = n - 1; i >= n - k; i --){
                ans = Math.max(ans, dp[i]);
            }
	    	return ans;
	    }
	}
```

C[100281. 矩阵中的最大得分](https://leetcode.cn/problems/maximum-difference-score-in-a-grid/)

给你一个由 **正整数** 组成、大小为 `m x n` 的矩阵 `grid`。你可以从矩阵中的任一单元格移动到另一个位于正下方或正右侧的任意单元格（不必相邻）。从值为 `c1` 的单元格移动到值为 `c2` 的单元格的得分为 `c2 - c1` 。

你可以从 **任一** 单元格开始，并且必须至少移动一次。

返回你能得到的 **最大** 总得分。

>    1.    $dp[i][j]$含义：以$i,j$为结束位置能获得的最大能量
>
>    2.    状态转移：当前位置可由上方或者左方转移过来，对于单个方向分成上一个点为起点或不是起点两种情况（为什么要分这两种情况呢，因为有可能从其他地方转移到上一个位置的分数为负数，还不如从上一个位置重新为起点开始计算）。计算四种情况的最大值则为$dp[i][j]$的值。
>
>          无论怎么转移分数都要减去上一个位置的数，加上当前位置的数。手动推一遍这个过程就能理解了QAQ。
>
>          $dp[i][j] = MAX(max(dp[i][j-1], 0)+ a[i][j]-a[i][j-1],max(dp[i-1][j],0)+a[i][j]-a[i-1][j])$
>
>    3.    初始化边界：转移方程比一般情况减少一个方向即可，另外$dp[0][0]=0$（因为不可能以这里为终点）
>
>    4.    结果取除了$dp[0][0]$的最大值
>
>    $O(mn)$

```java
class Solution {
    public int maxScore(List<List<Integer>> grid) {
        int n = grid.size();
        int m = grid.get(0).size();
        int a[][] = new int[n][m];
        for(int i = 0; i<n; i++)//转成数组方便取
            for(int j = 0; j<m; j++)
                a[i][j] = grid.get(i).get(j);
        int dp[][] = new int[n][m];
        dp[0][0] = 0;
        for(int i = 1; i<n; i++) 
            dp[i][0] = Math.max(dp[i - 1][0], 0) + a[i][0] - a[i - 1][0];//初始化边界
        for(int j = 1; j<m; j++)
            dp[0][j] = Math.max(dp[0][j - 1], 0) + a[0][j] - a[0][j - 1];//初始化边界
        //状态转移
        for(int i = 1; i<n; i++){
            for(int j = 1; j<m; j++){
                dp[i][j] = Math.max(dp[i - 1][j], 0) + a[i][j] - a[i - 1][j];
                dp[i][j] = Math.max(dp[i][j], Math.max(dp[i][j - 1], 0) + a[i][j] - a[i][j - 1]);
            }
        }
        int ans = -(int)1e9;
        for(int i = 0; i<n; i++){
            for(int j = 0; j<m; j++){
               if(i == 0 && j == 0) {continue;}
                ans = Math.max(ans, dp[i][j]);
            }
        }
        return ans;
    }
}
```

