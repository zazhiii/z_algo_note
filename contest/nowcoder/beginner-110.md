# [牛客小白月赛110](https://ac.nowcoder.com/acm/contest/101918) (exc：E F)

[C-智乃的数字_牛客小白月赛110](https://ac.nowcoder.com/acm/contest/101918/C)

> 找规律

```java
    public static void solve() throws IOException {
        int k = rd.nextInt();
        long n = (k - 1) / 7;
        long s = 30 * n;
        long[] t = new long[]{27, 3, 5, 9, 15, 21, 25};
        pw.println(s + t[k % 7]);
    }
```

[D-智乃与长短期主义者博弈_牛客小白月赛110](https://ac.nowcoder.com/acm/contest/101918/D)

> 区间dp

```java
    public static void solve() throws IOException {
        int n = rd.nextInt();
        int[] a = new int[n];
        int sum = 0;
        for(int i = 0; i < n; i ++) {
            a[i] = rd.nextInt();
            sum += a[i];
        }
        int[][] dp = new int[n + 1][n + 1]; // dp[i][j]: 长期主义者能在 i~j 区间内能获得的最大分数
        for(int i = 0; i < n; i ++) dp[i][i] = a[i];// 
        if(n == 1){
            pw.println(a[0] + " " + 0);
            return;
        }
        for(int len = 2; len <= n; len ++){
            for(int i = 0; i <= n - len; i ++){
                int l = i, r = i + len - 1;
                int selectLeft = a[l] + (a[l + 1] >= a[r] ? dp[l + 2][r] : dp[l + 1][r - 1]);
                int selectRight = a[r] + (a[l] >= a[r - 1] ? dp[l + 1][r - 1] : dp[l][r - 2]);
                dp[l][r] = Math.max(selectLeft, selectRight);
            }
        }
        int ans = a[0] >= a[n - 1] ? dp[1][n - 1] : dp[0][n - 2];
        pw.println(sum - ans + " " + ans);
    }
```

