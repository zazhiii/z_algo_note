# [✅第 416 场周赛](https://leetcode.cn/contest/weekly-contest-416/)

T2  二分答案  [3296. 移山所需的最少秒数 - 力扣（LeetCode）](https://leetcode.cn/problems/minimum-number-of-seconds-to-make-mountain-height-zero/description/)

T3 、T4 滑动窗口 [3298. 统计重新排列后包含另一个字符串的子字符串数目 II - 力扣（LeetCode）](https://leetcode.cn/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-ii/description/)

```java
class Solution {
    public long validSubstringCount(String w1, String w2) {
        int cnt[] = new int[128];
        int less = 0;
        for(int i = 0; i < w2.length(); i ++){
            if(cnt[w2.charAt(i)] == 0) less ++;
            cnt[w2.charAt(i)] ++;
        }
        long ans = 0;
        for(int l = 0, r = 0; r < w1.length(); r ++){
            cnt[w1.charAt(r)] --;
            if(cnt[w1.charAt(r)] == 0) less --;
            while(less == 0){
                if(cnt[w1.charAt(l)] == 0) less ++;
                cnt[w1.charAt(l)] ++;
                l ++;
            }
            ans += l;
        }
        return ans;
    }
}
```

