# 并查集模板

```java
    static int N = (int)1e5 + 10;
    static int p[] = new int[N], size[] = new int[N];
    static{
        // 若多组测试，放到单组测试中初始化，且初始化为当组所需大小
        for(int i = 0; i < N; i ++){
            p[i] = i;
            size[i] = 1;
        }
    }

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
```
