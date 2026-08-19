# 单调队列题单

用deque实现

```java
// 递增
for(int i = 0; i < n; i ++){
	if(!dq.isEmpty() && dq.getFirst() < i - m + 1) dq.pollFirst();
 	while(!dq.isEmpty() && a[dq.getLast()] >= a[i]) dq.pollLast();
 	dq.addLast(i);
} 
```



[洛谷 P1886](https://www.luogu.com.cn/problem/P1886) 【模板】
