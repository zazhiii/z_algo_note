# [Round 937 (Div. 4)](https://codeforces.com/contest/1950)（exc：F G）

[Problem - D - Codeforces](https://codeforces.com/contest/1950/problem/D)

给定一个$n$，判断$n$是否能分解成若干只由$01$组成的数的乘积。

> 枚举
>
> 枚举出所有$10^5$以内的由$01$组成的数（除0和1，可以用二进制枚举），$n$从大到小试除，判断最后$n$能否被除为$1$

```java
    static List<Integer> d = new ArrayList<>();
    static {
        for(int i = (1 << 5) - 1; i >= 2; i --){
            int t = 0;
            for(int j = 0; j < 5; j ++){
                if((i >> j & 1) == 1) t += Math.pow(10, j);
            }
            d.add(t);
        }
    }
    static public void solve() throws IOException{
        int n = rd.nextInt();
        for(int x : d){
            while(n % x == 0) n /= x;
        }
        pw.println(n == 1 ? "YES" : "NO");
    }
```

> DFS
>
> 枚举出所有$10^5$以内的由$01$组成的数，dfs枚举出若干这些数能组成的所有数（这两步都是预处理），这样就可以$O(1)$判断答案

```java
    static List<Integer> d = new ArrayList<>();
    static Set<Long> set = new HashSet<>();
    static int maxn = (int)1e5;
    static {
        for(int i = (1 << 5) - 1; i >= 2; i --){
            int t = 0;
            for(int j = 0; j < 5; j ++){
                if((i >> j & 1) == 1) t += Math.pow(10, j);
            }
            d.add(t);
        }
        dfs(1);
    }
    public static void dfs(long mul){
        if(mul > maxn) return;
        set.add(mul);
        for(int x : d){
            dfs(mul * x);
        }
    }
    static public void solve() throws IOException{
        int n = rd.nextInt();
        pw.println(set.contains(1L * n) ? "YES" : "NO");
    }
```

[Problem - E - Codeforces](https://codeforces.com/contest/1950/problem/E)

给定一个长度$n$的字符串$s$，求一个字符串$k$，使得拼接若干个$k$能等于$s$ 或者 只与$s$有一个位置的字母不同。

> 枚举
>
> 实现比思路难；枚举$n$的因数再判断是否满足条件，假设是$x$段长度为$l$的$k$拼凑，其中最多只允许有$1$段和其他$x-1$段不同，且只有一个字母不同。枚举每一段的$[0,1,...,l-1]$这些位置，单独判断每个位置的字母是否满足条件，总体是否满足条件。

```java
 static public void solve() throws IOException{
        int n = rd.nextInt();
        String s = rd.next();
        List<Integer> d = new ArrayList<>();
        for(int i = 1; i <= n / i; i ++){
            if(n % i == 0) {
                d.add(i);
                if(i * i < n) d.add(n / i);
            }
        }
        int f[] = new int[26];
        for(int i = 0; i < n; i ++) f[s.charAt(i) - 'a'] ++;
        Collections.sort(d); 
        for(int x : d){
            int t = 0;
            boolean ok = true;
            for(int i = 0; i < x; i ++){
                Map<Character, Integer> map = new HashMap<>();
                for(int j = i; j < n; j += x){
                    map.put(s.charAt(j), map.getOrDefault(s.charAt(j), 0) + 1);
                }
                if(map.size() > 2){
                    ok = false;
                }else if(map.size() == 2){
                    t ++;
                    for(char c : map.keySet()){
                        if(map.get(c) != 1 && map.get(c) != n / x - 1) ok = false;
                    }
                }
            }
            if(t <= 1 && ok){
                pw.println(x);
                return;
            }
        }
    }
```

