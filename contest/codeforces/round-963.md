# [Round 963 (Div. 2)](https://codeforces.com/contest/1993)

[Problem - B - Codeforces](https://codeforces.com/contest/1993/problem/B)

给定一个由 n 个正整数组成的数组 a 。

在一次操作中，你可以选取任意一对索引 $(i,j)$，且 $a_i$ 和 $a_j$ 具有**不同的**奇偶性，然后用它们的和替换较小的那个。

求使数组中所有元素具有相同奇偶性所需的最少操作数。

> 思维、贪心

> 首先合并两个奇偶不一的数得到的一定是一个奇数，那么最终结果一定是将数组中所有偶数都变为奇数。
>
> 我们将合并操作理解为一个较大数吃掉较小数，产生一个新的合并的数。贪心地，尽量用奇数去吃掉偶数，这样会直接减少一个偶数；而用偶数去吃奇数不会减少偶数个数。
>
> 接下来我们去判断一个尽量大地奇数是否能够将所有偶数吃完。首先，如果数组中地最大值是奇数，那么毫无疑问它可以吃掉所有偶数，吃地次数等于偶数个数。若最大值不是奇数，我们就用最大的奇数从小到大地吃偶数，过程中维护它吃了偶数之后变大地值，直到不能再吃偶数。如果它不能将偶数吃完，也就是吃到不能再吃了也无法大于最大的偶数值。那么就需要用最大的偶数值与一个较小的奇数值造一个最大的奇数出来，将剩余偶数吃掉，这个过程用了偶数数量+1次操作

> $O(n)$

```java
import java.io.*;
import java.util.*;

public class Prac {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    public static void solve(){
        int n = sc.nextInt();
        int a[] = new int[n];
        int odd = 0, mxodd = 0;
        for(int i = 0; i < n; i ++) {
            a[i] = sc.nextInt();
            if(a[i] % 2 == 1) {
                odd ++;
                mxodd = Math.max(mxodd, a[i]);
            }
        }
        Arrays.sort(a);
        if(odd == 0) {
            pw.println(0);
            return;
        }
        if(a[n - 1] % 2 == 1) pw.println(n - odd);
        else{
            long sum = mxodd;
            for(int i = 0; i < n; i ++){
                if(a[i] % 2 == 0 && a[i] < sum) sum += a[i]; 
            }
            pw.println(sum > a[n - 1] ? n - odd : n - odd + 1);
        }
    }
    public static void main(String[] args) throws IOException {     
        int T = sc.nextInt();
        while(T --> 0) solve();
        pw.flush();pw.close();
    }
}

```

[Problem - C - Codeforces](https://codeforces.com/contest/1993/problem/C)

有一个由 n 个房间组成的公寓，每个房间的灯最初都是关着的。

为了控制这些房间的灯光，公寓的主人决定在房间里安装芯片，这样每个房间正好有一个芯片，芯片安装在不同的时间。具体来说，这些时间由数组 a1,a2,…,an 表示，其中 ai 是在 i /th房间安装芯片的时间(以分钟为单位)。

芯片安装后，每隔 kk 分钟就会改变房间的灯光状态--在 kk 分钟内打开灯光，然后在接下来的 kk 分钟内关闭灯光，再在接下来的 kk 分钟内重新打开灯光，以此类推。换句话说，芯片在 ai 、 ai+k 、 ai+2k 、 ai+3k 、 …… 分钟时改变 i /th房间的灯光状态。

公寓里所有房间最早亮灯的时刻是什么时候？

> 模拟？

> 求最早时刻所有灯都处于亮的状态。首先一定是在安装最后一个灯泡后出现这个时刻，且一定是出现在最后这个灯的第一个亮区间内。因为所有灯的周期是一样的，那么整体情况也会有一个周期且为$2k$，在最后这个灯的每个明亮区间内，所有灯的状态变化是一致的。如果第一个明亮区间没有出现全亮，就不可能出现全亮了。
>
> 我们求最后一个灯炮的第一个明亮区间和前面每个灯泡在这个时间区间内明亮区间的交集即可。

> $O(n\log n)$

```java
import java.io.*;
import java.util.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    public static void solve(){
        int n = sc.nextInt();
        int k = sc.nextInt();
        int a[] = new int[n];
        for(int i = 0 ; i < n; i ++) a[i] = sc.nextInt();
        Arrays.sort(a);
        int l = a[n - 1], r = a[n - 1] + k;
        for(int i = n - 2; i >= 0; i --){
            int x = (a[n - 1] - a[i]) / k;
            if(x % 2 == 0){
                r = Math.min(r, a[i] + x * k + k);
            }else{
                l = Math.max(l, a[i] + x * k + k);
            }
        }
        pw.println(l < r ? l : -1);
    }
    public static void main(String[] args) throws IOException {     
        int T = sc.nextInt();
        while(T --> 0) solve();
        pw.flush();pw.close();
    }
}

```

