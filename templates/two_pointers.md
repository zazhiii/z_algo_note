# 双指针模板

## 最长连续不重复子序列

给定一个长度为 $n$ 的整数序列，找出最长的不包含重复的数的连续区间

> 维护所有元素数量不超过1的最大区间长度

```java
// a[] 整数序列
// s[] 记录每个数出现几次
for(int i = 0, j = 0; i < n; i ++){
    s[a[i]] ++;
    while(s[a[i]] > 1){ // 若有数出现次数大于2次，那么一定是新出现这个数
        s[a[j]] --;     // 移动左指针直到出现2次的数减小为1次
        j ++;   
    }
    ans = Math.max(ans, i - j + 1);   
}
pw.println(ans);
```

[LeetCode maximum-length-substring-with-two-occurrences](https://leetcode.cn/problems/maximum-length-substring-with-two-occurrences/description/)

## 判断子序列

判断`a[]`是否为`b[]`的子序列

```java
int i = 0, j = 0;
while(i < n && j < m){
    if(a[i] == b[j]) i ++;
    j ++;    
}
pw.println(i == n ? "Yes" : "No");
```
