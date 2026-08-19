# 进制转换



读取$n$进制的数字字符串$s$为`Integer`或者`Long`

```java
// Long.valueOf(String s, int radix)
Long.valueOf(k, n)
// Integer.valueOf(String s, int radix)
Integer.valueOf(k, n)
```



数字`i`转换为`radix`进制

```java
Long.toString(long i, int radix);
Integer.toString(int i, int radix);
```



相关题目：

[洛谷 P1143](https://www.luogu.com.cn/problem/P1143)