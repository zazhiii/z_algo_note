# 牛客练习赛129（exc: E F）

[C-和天下_牛客练习赛129 (nowcoder.com)](https://ac.nowcoder.com/acm/contest/90074/C)

> 设$k$的最高位$1$位置为第$hi$位：0000......0000**1**000010000100
>
> 考虑在一个位中能合并哪些数，将能合并的数放到一个二进制位中（64个位置）；
>
> 对于$a_i$：
>
> - 对于高于$hi$的位置$j(63\ge j >hi)$，所有在$j$位置为$1$的数能放在$j$位中合并（这个好理解，因为并操作之后直接肯定大于$k$)
> - 低于或等于$hi$的位置$j'$，除了满足$j'$位是$1$之外，还需满足在$j'$之前$k$是$1$的位$a_i$在这个位也必须是$1$，并且$k$在$j'$位为0，（前者额外条件保证了在$j'$位置合并的数不小于$k$，后者额外条件保证了满足前者额外条件下在$j'$为位置合并的数大于$k$）；如果碰到$k$在某个位是$1$而$a_i$在该位是$0$那么就不用考虑后面的位了。
>
> `k--`是为了考虑在k的lowbit位置合并的那些数，等于$k$的数包含在这些数中
>
> 合并的位置可以用一个数组来单独装，每个位置只需要装一个元素即可；

```java
    static int N = (int)2e5 + 100;
    static int p[] = new int[N], size[] = new int[N];
    public static int find(int x){
        if(p[x] != x) p[x] = find(p[x]);
        return p[x];
    }
    public static void union(int x, int y){
        int fx = find(x), fy = find(y);
        if(fx != fy){
            p[fx] = fy;
            size[fy] += size[fx];
        }
    }
    public static void solve() throws IOException{
        int n = rd.nextInt();
        long k = rd.nextLong();
        k --;
 
        for(int i = 0; i < n + 100; i ++){
            p[i] = i;
            size[i] = 1;
        }
 
        long a[] = new long[n + 1];
        for(int i = 1; i <= n; i ++)a[i] = rd.nextLong();
 
        if(k < 0){pw.println(n); return;}

        int v[] = new int[64];
        Arrays.fill(v, -1);
 
        for(int i = 1; i <= n; i ++){
            for(int j = 63; j >= 0; j --){
                long l = (a[i] >> j) & 1, r = (k >> j) & 1;
                if(r == 1 && l == 0) break;
                if(r == 0 && l == 1) {
                    if(v[j] == -1) v[j] = i;
                    else union(i, v[j]);
                }
            }
        }
        long ans = 0;
        for(int i = 1; i <= n; i ++){
            ans = Math.max(ans, size[find(i)]);
        }
        pw.println(ans);    
    }
```

[D-搬家_牛客练习赛129 (nowcoder.com)](https://ac.nowcoder.com/acm/contest/90074/D)

> 双指针预处理、倍增

```java
    static int n, m, k;
    static long pre[];
    public static void solve() throws IOException{     
        n = rd.nextInt();
        m = rd.nextInt();
        k = rd.nextInt();
        pre = new long[n + 1];
        int a[] = new int[n + 1];
        for(int i = 1; i <= n; i ++) {
            a[i] = rd.nextInt();;
            pre[i] = pre[i - 1] + a[i];
        }
        int t = 20;
        int st[][] = new int[n + 1][t + 1];
        for(int i = 1, j = 1; i <= n; i ++){
            while(j <= n && pre[j] - pre[i - 1] <= k) j ++;
            st[i][0] = j - 1;
        }
        for(int j = 1; j <= t; j ++){
            for(int i = 1; i <= n; i ++){
                // 从2^(j - 1)步跳到st[i][j - 1]，再从st[i][j - 1] + 1位置再跳2^(j - 1)步
                st[i][j] = st[Math.min(n, st[i][j - 1] + 1)][j - 1];
            }
        }        
        int ans = 0;
        for(int i = 1; i <= n; i ++){
            int p = i; // 从p位置开始跳
            for(int j = t; j >= 0; j --){
                if((m >> j & 1) == 1){ // 将m步拆解为2的x次幂的步数，例如7 => 2^2 + 2^1 + 2^0
                    p = st[p][j] + 1; // 从p位置跳2^j步到st[p][j], 下一次再从st[p][j] + 1处开始跳
                }
                if(p > n) break;  // 跳到最后了就退出，防止st[n + 1][j]越界
            }
            ans = Math.max(ans, p - i);
        }
        pw.println(ans);
    }
```

