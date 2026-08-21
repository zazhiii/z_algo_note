# Java 集合与数组



## Array

### Arrays类

比较两个数组元素是否全部相等

```java
int[] a = {}, b = {};
Arrays.equals(a, b);
```



## `TreeSet`



构造器

```java
public TreeSet() // 1. 普通的构造器
public TreeSet(Comparator <? super E > comparator) // 2. 可以传入比较器，指定排序规则
```

方法

基本操作（`add`、`remove` 和 `contains`）复杂度为$\log(n)$ 

```java
E ceiling(E e) // 返回集合中大于或等于e的最小元素，若没有则返回null
E floor(E e) // 返回集合中小于或等于e的最大元素，若没有则返回null
E higher(E e) // 返回集合中严格大于e的最小元素，若没有则返回null
E lower(E e) // 返回集合中严格小于e的最小元素，若没有则返回null
```

题目

[D - Cross Explosion (atcoder.jp)](https://atcoder.jp/contests/abc370/tasks/abc370_d) 

[P2234 [HNOI2002] 营业额统计 - 洛谷 | 计算机科学教育新生态](https://www.luogu.com.cn/problem/P2234) 

[P5250 【深基17.例5】木材仓库 - 洛谷 | 计算机科学教育新生态](https://www.luogu.com.cn/problem/P5250) 

