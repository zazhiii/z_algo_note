# 双指针与滑动窗口题单



## 滑动窗口

> 解决子数组和子串问题

### 不定长滑窗

#### 经典例题

[3. 无重复字符的最长子串 - 力扣（LeetCode）](https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/) 

[3090. 每个字符最多出现两次的最长子字符串 - 力扣（LeetCode）](https://leetcode.cn/problems/maximum-length-substring-with-two-occurrences/description/)

[76. 最小覆盖子串 - 力扣（LeetCode）](https://leetcode.cn/problems/minimum-window-substring/) 

[134. 加油站 - 力扣（LeetCode）](https://leetcode.cn/problems/gas-station/submissions/) 判断是否有长度>=n的子数组满足其前缀和都>=0

[1234. 替换子串得到平衡字符串 - 力扣（LeetCode）](https://leetcode.cn/problems/replace-the-substring-for-balanced-string/) 转化为[76.最小覆盖子串]，最小子串覆盖所有超过n/4的部分

[992. K 个不同整数的子数组 - 力扣（LeetCode） ](https://leetcode.cn/problems/subarrays-with-k-different-integers/description/) 求不同数字数等于k 转化为 不同数字数<=k 减去 不同数字数 <= k - 1

待做	[395. 至少有 K 个重复字符的最长子串 - 力扣（LeetCode）](https://leetcode.cn/problems/longest-substring-with-at-least-k-repeating-characters/description/)

---

[2962. 统计最大元素出现至少 K 次的子数组 - 力扣（LeetCode）](https://leetcode.cn/problems/count-subarrays-where-max-element-appears-at-least-k-times/description/) [学习滑窗思想]  

[3298. 统计重新排列后包含另一个字符串的子字符串数目 II - 力扣（LeetCode）](https://leetcode.cn/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-ii/description/) [76题的计数版本]

[P2058 [NOIP 2016 普及组] 海港 - 洛谷 | 计算机科学教育新生态](https://www.luogu.com.cn/problem/P2058) 黄



#### 求最长/最大

>  移动一次右端点，缩减左端点至区间合法之后记录答案

 [3090. 每个字符最多出现两次的最长子字符串](https://leetcode.cn/problems/maximum-length-substring-with-two-occurrences/)  类似：3. 无重复字符的最长子串

[1493. 删掉一个元素以后全为 1 的最长子数组 - 力扣（LeetCode）](https://leetcode.cn/problems/longest-subarray-of-1s-after-deleting-one-element/)  包含<=1个0的最长子串

[1208. 尽可能使字符串相等 - 力扣（LeetCode）](https://leetcode.cn/problems/get-equal-substrings-within-budget/description/)  总和不超过max的最长子数组

[2730. 找到最长的半重复子字符串 - 力扣（LeetCode）](https://leetcode.cn/problems/find-the-longest-semi-repetitive-substring/description/) 

[904. 水果成篮 - 力扣（LeetCode）](https://leetcode.cn/problems/fruit-into-baskets/description/) 1516 包含不超过2种数字的最长子数组

[1695. 删除子数组的最大得分 - 力扣（LeetCode）](https://leetcode.cn/problems/maximum-erasure-value/description/) 1529 无重复数字子数组最大和

[2958. 最多 K 个重复元素的最长子数组 - 力扣（LeetCode）](https://leetcode.cn/problems/length-of-longest-subarray-with-at-most-k-frequency/description/) 1535 

[2024. 考试的最大困扰度 - 力扣（LeetCode）](https://leetcode.cn/problems/maximize-the-confusion-of-an-exam/description/) 1643 维护 某个元素的个数不超过k的 最大区间

[1004. 最大连续1的个数 III - 力扣（LeetCode）](https://leetcode.cn/problems/max-consecutive-ones-iii/description/) 1656 包含不超过k个0的最长子串

[1658. 将 x 减到 0 的最小操作数 - 力扣（LeetCode）](https://leetcode.cn/problems/minimum-operations-to-reduce-x-to-zero/description/) 1817 和恰好为`sum - x` 的最长子数组

[1838. 最高频元素的频数 - 力扣（LeetCode）](https://leetcode.cn/problems/frequency-of-the-most-frequent-element/) 1879 

[2516. 每种字符至少取 K 个 - 力扣（LeetCode）](https://leetcode.cn/problems/take-k-of-each-character-from-left-and-right/description/) 1948 每种字符最多出现$sum_i-k$次的最长子数组

[2831. 找出最长等值子数组 - 力扣（LeetCode）](https://leetcode.cn/problems/find-the-longest-equal-subarray/description/) 1976 分组+枚举每个数n次滑窗



[Problem - C - Codeforces](https://codeforces.com/contest/2025/problem/C)	1300；"最长"、"连续"、"出现不超过k个数" 的子序列



#### 求最短/最小

> 移动一次右端点，缩减左端点到最后一次合法(再移动左端点就不合法)，记录答案

[209. 长度最小的子数组 - 力扣（LeetCode）](https://leetcode.cn/problems/minimum-size-subarray-sum/description/) 

[2904. 最短且字典序最小的美丽子字符串 - 力扣（LeetCode）](https://leetcode.cn/problems/shortest-and-lexicographically-smallest-beautiful-string/description/) 1482

[2875. 无限数组的最短子数组 - 力扣（LeetCode）](https://leetcode.cn/problems/minimum-size-subarray-in-infinite-array/description/) 1914 

#### 计数类

> 移动一次右端点，移动左端点到分界点，统计答案

[1358. 包含所有三种字符的子字符串数目 - 力扣（LeetCode）](https://leetcode.cn/problems/number-of-substrings-containing-all-three-characters/description/) 1646

[2799. 统计完全子数组的数目 - 力扣（LeetCode）](https://leetcode.cn/problems/count-complete-subarrays-in-an-array/description/) $O(n)$做法

[2537. 统计好子数组的数目 - 力扣（LeetCode）](https://leetcode.cn/problems/count-the-number-of-good-subarrays/description/) 1892

[C - Various Kagamimochi](https://atcoder.jp/contests/abc388/tasks/abc388_c) 

---

[713. 乘积小于 K 的子数组 - 力扣（LeetCode）](https://leetcode.cn/problems/subarray-product-less-than-k/description/)

[2302. 统计得分小于 K 的子数组数目 - 力扣（LeetCode）](https://leetcode.cn/problems/count-subarrays-with-score-less-than-k/description/) 1808

[2762. 不间断子数组 - 力扣（LeetCode）](https://leetcode.cn/problems/continuous-subarrays/description/) 1940 单调队列维护区间最值

#### 恰好型

[930. 和相同的二元子数组 - 力扣（LeetCode）](https://leetcode.cn/problems/binary-subarrays-with-sum/description/) 1592 滑窗 | 前缀和 + 哈希表

[1248. 统计「优美子数组」 - 力扣（LeetCode）](https://leetcode.cn/problems/count-number-of-nice-subarrays/description/) 1624 同上一题

[3306. 元音辅音字符串计数 II - 力扣（LeetCode）](https://leetcode.cn/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/description/) 2200

[992. K 个不同整数的子数组 - 力扣（LeetCode）](https://leetcode.cn/problems/subarrays-with-k-different-integers/description/) 2210



## 双指针

[922. 按奇偶排序数组 II - 力扣（LeetCode）](https://leetcode.cn/problems/sort-array-by-parity-ii/) 用两个奇偶指针操作
