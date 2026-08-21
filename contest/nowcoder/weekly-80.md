# [牛客周赛 Round 80](https://ac.nowcoder.com/acm/contest/101196) (exc: F G)

[C-举手赢棋easy_牛客周赛 Round 80](https://ac.nowcoder.com/acm/contest/101196/C) 

> 遍历，`lo`记录`0`数量`wi`记录`1`数量，变量`k`记录举了几次手。在第一次遇到`lo == wi + 1`时选择举手，可以选择在此之前的任何一个`0`位置举手，也就是`lo`，如果在此遇到这种情况那就没办法满足条件了，输出`0`结束程序。如果遍历完了都没遇到这种情况，那么就可以在任意位置举手，即`n`种情况。
>
> $O(n)$

```java
 public static void solve() throws IOException {
        int n = rd.nextInt();
        char[] c = rd.next().toCharArray();
        int lo = 0, wi = 0, k = 0, ans = 0;
        for (int i = 0; i < n; i++) {
            if (c[i] == '1')
                wi++;
            else
                lo++;
            if (lo == wi + 1) {
                if (k == 0) { // 没有举过手
                    ans += lo; // 在此之前的任意0位置举手都可以
                    wi++;
                    lo--;
                    k++;
                } else { // 举过手了还遇到这种情况，这就没办法保持任意时刻满足条件了
                    pw.println(0);
                    return;
                }
            }
        }
        pw.println(ans == 0 ? n : ans);
    }
```

[D-举手赢棋hard_牛客周赛 Round 80](https://ac.nowcoder.com/acm/contest/101196/D)

> 类似的，我们依然用 `wi lo k` 记录对应值。当第一次遇到必须举手的情况即`k == 0 && lo == wi + 1`时，可以有个此时的 `lo` 个位置可以举手，用`p1 == lo`记录（此时 `0` 的个数）。第二次，即 `k == 1 && lo == wi + 1` 时，用 `p2 == lo` 记录第二次可以举手的位置数。这样第一次举手就可以有`p1`个位置可以选，第二次举手可以有`p2`个位置可以选。型如：
>
> ```
> axaaa
> b bbbbbxbbbb
> 第一次必须在a范围内选一个，第二次必须在b范围内选一个, 并且不能选同一个位置
> ```
>
> 如果这两次举手是不同的，那么答案就是$p1\times p2$，但它是视作相同的，那么如果二者都现在a范围内就会重复一部分，会重复$C_{p1}^2$个情况，减掉即可。（这里肯定还有其他算法，只要不重复就行）
>
> 特别的：如果`p1 == 0` 那么 第一次就有`n`个选择，第二次有`n - 1`个选择。单独的`p2 == 0`那么第二次依然有`n - 1`中选择。
>
> $O(n)$

```java
    public static void solve() throws IOException {
        int n = rd.nextInt();
        char[] c = rd.next().toCharArray();
        int lo = 0, wi = 0, k = 0, p1 = 0, p2 = 0;
        for (int i = 0; i < n; i++) {
            if (c[i] == '1')
                wi++;
            else
                lo++;
            if (lo == wi + 1) {
                if (k == 0) {
                    p1 = lo; 
                    wi ++;
                    lo --;
                    k ++;
                } else if(k == 1) { 
                    p2 = lo;
                    wi ++;
                    lo --;
                    k ++;
                } else { // 超过两次不行
                    pw.println(0);
                    return;
                }
            }
        }
        if(p1 == 0) p1 = n;
        if(p2 == 0) p2 = n - 1;
        pw.println(1L * p1 * p2 - 1L * p1 * (p1 - 1) / 2);
    }
```

 [E-公平对局_牛客周赛 Round 80](https://ac.nowcoder.com/acm/contest/101196/E)

> BFS记录每个白子联通块的数量以及边界空位的数量以及空位的位置。若空位刚好只有一个就记录答案。
>
> 特别的要注意一个空位能吃两个连通块的情况：
>
> ```
> 5
> #####
> #*#*#
> #*.*#
> #*#*#
> #####
> ```
>
> 这种情况我们将每次BFS的白子数量叠加到缺口再记录答案即可。
>
> $O(n^2)$

```java
    static int n;
    static char[][] c;
    static int[] dx = { 1, -1, 0, 0 }, dy = { 0, 0, 1, -1 };

    public static void solve() throws IOException {
        n = rd.nextInt();
        c = new char[n][n];
        for (int i = 0; i < n; i++) {
            c[i] = rd.next().toCharArray();
        }

        boolean[][] f = new boolean[n][n];
        int[][] sum = new int[n][n];

        int ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (f[i][j] || c[i][j] != '*')
                    continue;

                Queue<int[]> que = new ArrayDeque<>();
                que.add(new int[] { i, j });
                f[i][j] = true;
                int ept = 0, eptx = 0, epty = 0, cnt = 0; // 缺口数, 缺口位置, 白子数量
                boolean[][] fept = new boolean[n][n];

                while (!que.isEmpty()) {
                    cnt++;
                    int[] t = que.poll();
                    int x = t[0], y = t[1];

                    for (int k = 0; k < 4; k++) {
                        int nx = x + dx[k];
                        int ny = y + dy[k];
                        if (nx < 0 || nx >= n || ny < 0 || ny >= n || c[nx][ny] == '#' || f[nx][ny])
                            continue;
                        if (c[nx][ny] == '.') {
                            if (!fept[nx][ny]) {
                                fept[nx][ny] = true;
                                ept++;
                                eptx = nx; // 记录缺口位置
                                epty = ny;
                            }
                            continue;
                        }
                        que.add(new int[] { nx, ny });
                        f[nx][ny] = true;
                    }
                }
                if (ept == 1) {
                    sum[eptx][epty] += cnt;
                    ans = Math.max(ans, sum[eptx][epty]);
                }
            }
        }
        pw.println(ans);
    }
```

[G-不公平对局_牛客周赛 Round 80](https://ac.nowcoder.com/acm/contest/101196/G) 

