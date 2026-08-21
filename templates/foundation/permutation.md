# `next_permutation`

这个函数会将传入的数组变为下一个字典序的排列并返回`true`；若已经是最后一个字典序了，则不对元数组做修改并返回`false`。

配合`do while`语句可以达到枚举所有排列的效果。

注：这个函数在Java中没有内置，需要手写实现。在C++中是标准库中的一个函数。



## 示例：

```java
int[] a = {1, 2, 2, 3};

do{
    System.out.println(Arrays.toString(a));
}while(nextPermutation(a));

// 输出结果：
[1, 2, 2, 3]
[1, 2, 3, 2]
[1, 3, 2, 2]
[2, 1, 2, 3]
[2, 1, 3, 2]
[2, 2, 1, 3]
[2, 2, 3, 1]
[2, 3, 1, 2]
[2, 3, 2, 1]
[3, 1, 2, 2]
[3, 2, 1, 2]
[3, 2, 2, 1]
```



## 实现

`int`类型

```java
    public static boolean nextPermutation(int a[]){
        int n = a.length, i = n - 2;
        while(i >= 0 && a[i] >= a[i + 1]) i --; 
        if(i < 0) return false;
        int k = i + 1;
        while(k < n && a[k] > a[i]) k ++;
        {int t = a[i]; a[i] = a[k - 1]; a[k - 1] = t;} // swap(a[i], a[k - 1])
        Arrays.sort(a, i + 1, n);
        return true;
    }
```

`char`类型

```java
    public static boolean nextPermutation(char a[]){
        int n = a.length, i = n - 2;
        while(i >= 0 && a[i] >= a[i + 1]) i --;
        if(i < 0) return false;
        int k = i + 1;
        while(k < n && a[k] > a[i]) k ++;
        {char t = a[i]; a[i] = a[k - 1]; a[k - 1] = t;} // swap(a[i], a[k - 1])
        Arrays.sort(a, i + 1, n);
        return true;
    }
```

其他类型类似……