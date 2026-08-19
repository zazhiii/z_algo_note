# 排列与置换题单

[C - Make Isomorphic (atcoder.jp)](https://atcoder.jp/contests/abc371/tasks/abc371_c)

---

## next_permutation应用

[P1088 [NOIP2004 普及组] 火星人 - 洛谷 | 计算机科学教育新生态 (luogu.com.cn)](https://www.luogu.com.cn/problem/P1088)





## 置换环

**置换环**是用来求解**数组排序元素间所需最小交换次数**这类问题。

置换环思想：置换环将每个元素指向其排序后应在的位置，最终首尾相连形成一个环**（若数字在最终位置，则其自身成环）**

元素间的交换只在同一个环内进行。

每个环内的最小交换次数为：`环上的元素 - 1`，使整个序列有序需要最小交换次数：`元素总个数 - 环的个数`



[E - Sakurako, Kosuke, and the Permutation](https://codeforces.com/contest/2033/problem/E)
