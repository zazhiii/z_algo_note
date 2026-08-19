# Java 字符串

## `String` 实例方法

创建实例后，通过实例调用的方法

```java
int length() // 获取字符串长度

String[] split(String regex) // 围绕给定 正则表达式 的匹配项拆分此字符串，转义字符要加\\
```

## `String` 静态方法

通过`String.xxx`调用的方法

> 暂无条目，后续补充常用静态方法。

## 可变字符串

`String`对象一旦创建就是不可变的，若对其进行修改操作，实际上是创建了新的`String`对象。由于这个特性，大量字符串拼接效率是非常低的。`StringBuilder`类和`StringBuffer`类则解决了这个问题，你可以对他们同一个对象进行修改而不创建新的对象。二者具有相同的功能，但他们一个重要的区别是`StringBuilder`不是线程安全的而`StringBuffer`是线程安全的，相较而言`StringBuilder`有更优的性能。一般来说，在写算法题时没有线程安全的要求，**推荐使用 `StringBuilder` 。**

1. 构造方法 **创建StringBuilder**

`StringBuilder()` 无参构造

`StringBuilder(String str)` 指定初始值

```java
StringBuilder sb = new StringBuilder();
StringBuilder sb = new StringBuilder("Hello world!");
```

2. 实例方法

增

`StringBuilder append(XXX xxx)` **拼接**，支持大部分基本类型、String、StringBuilder

删

`StringBuilder delete(int start, int end)` 删除指定位置字符串，同上为`[start, end)`位置

`StringBuilder deleteCharAt(int index)` 删除指定位置字符

改

`StringBuilder reverse()` 反转

`StringBuilder replace(int start, int end, String str)` 替换指定位置字符串，注意为`[start, end)`不包含`end`位置

`StringBuilder insert(int offset, XXX xxx)` 插入字符串
