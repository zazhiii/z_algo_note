# ✅第 400 场周赛

B	[100311. 无需开会的工作日](https://leetcode.cn/problems/count-days-without-meetings/)

给你一个正整数 `days`，表示员工可工作的总天数（从第 1 天开始）。另给你一个二维数组 `meetings`，长度为 `n`，其中 `meetings[i] = [start_i, end_i]` 表示第 `i` 次会议的开始和结束天数（包含首尾）。

返回员工可工作且没有安排会议的天数

>    **区间合并**
>
>    按照左端点排序，遍历每个区间，分类讨论一下下一个区间和当前区间的关系，答案加上超出的部分。
>
>    $O(m\log m + m) $

```java
class Solution {
    public int countDays(int days, int[][] meetings) {
        int n = meetings.length;
        Arrays.sort(meetings, (m1, m2) -> m1[0] - m2[0]);
        int ans = days;
        int r = 0;
        for(int i = 0; i < n; i ++){
            if(meetings[i][0] > r){
                ans -= meetings[i][1] - meetings[i][0] + 1;
                r = meetings[i][1];
            }else if(meetings[i][1] > r){
                ans -= meetings[i][1] - r;
                r = meetings[i][1];
            }
        }
        return ans;
    }
}
```

C	[100322. 删除星号以后字典序最小的字符串](https://leetcode.cn/problems/lexicographically-minimum-string-after-removing-stars/)

给你一个字符串 `s` 。它可能包含任意数量的 `'*'` 字符。你的任务是删除所有的 `'*'` 字符。

当字符串还存在至少一个 `'*'` 字符时，你可以执行以下操作：

-    删除最左边的 `'*'` 字符，同时删除该星号字符左边一个字典序 **最小** 的字符。如果有多个字典序最小的字符，你可以删除它们中的任意一个。

请你返回删除所有 `'*'` 字符以后，剩余字符连接而成的 字典序最小 的字符串。

>    显然删除靠后的最小字幕最优。
>
>    遍历，用26个栈存储每种字母的下标，遇到*则弹出字典序最小的字母对应的非空栈的栈顶元素（即最靠后的），弹出后用一个数组标记位置，计算答案时忽略该位置。

```java
class Solution {
    public String clearStars(String s) {
        char c[] = s.toCharArray();
        int n = s.length();
        boolean[] k = new boolean[n];
        List<Integer>[] words = new LinkedList[26];
        for(int i = 0; i < 26; i ++){
            words[i] = new LinkedList<>();
        }
        for(int i = 0; i < n; i ++){
            if(c[i] != '*'){
                words[c[i] - 'a'].add(i);
            }else{
                for(int j = 0; j < 26; j ++){
                    if(!words[j].isEmpty()){
                        k[words[j].get(words[j].size() - 1)] = true;
                        words[j].remove(words[j].size() - 1);
                        break;
                    }
                }
            }
        }
        String ans = "";
        for(int i = 0; i < n; i ++){
            if(c[i] != '*' && !k[i]) ans += c[i];
        }
        return ans;
    }
}
```

T4  [3171. 找到按位或最接近 K 的子数组 - 力扣（LeetCode）](https://leetcode.cn/problems/find-subarray-with-bitwise-or-closest-to-k/description/)

给你一个数组 `nums` 和一个整数 `k` 。你需要找到 `nums` 的一个 子数组 ，满足子数组中所有元素按位或运算 `OR` 的值与 `k` 的 **绝对差** 尽可能 **小** 。换言之，你需要选择一个子数组 `nums[l..r]` 满足 `|k - (nums[l] OR nums[l + 1] ... OR nums[r])|` 最小。

请你返回 **最小** 的绝对差值。

> LogTrick

```java
class Solution {
    public int minimumDifference(int[] a, int k) {
        int ans = (int)1e9;
        for(int i = 0; i < a.length; i ++){
            ans = Math.min(ans, Math.abs(a[i] - k));
            // 若a[i]是 (a[j] | a[j + 1] | ... | a[i - 1])的子集，那么就不必枚举以a[i]结尾更长的子数组了
            for(int j = i - 1; j >= 0 && ((a[i] | a[j]) != a[j]); j --){
                a[j] |= a[i]; // a[j]存储的 a[j] | a[j + 1] | ... | a[i], 
                ans = Math.min(ans, Math.abs(a[j] - k));
            }
        }
        return ans;
    }
}
```

