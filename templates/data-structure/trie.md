# Trie

```java
	public static int N = (int)1e6;
	public static int nex[][] = new int[N][26], pass[] = new int[N], end[] = new int[N], cnt = 0;

    /* 将字符串加入trie */
	public static void add(String s) {
        int p = 0;
        pass[p] ++;
        for(int i = 0; i < s.length(); i ++){
            int c = s.charAt(i) - 'a';
            if(nex[p][c] == 0) nex[p][c] = ++cnt;
            p = nex[p][c];
            pass[p] ++;
        }
        end[p] ++;
	}

    /* 查询s出现过几次 */
	public static int find(String s) {
        int p = 0;
        for(int i = 0; i < s.length(); i ++){
            int c = s.charAt(i) - 'a';
            if(nex[p][c] == 0) return 0;
            p = nex[p][c];
        }
        return end[p];
	}

    /* 返回以pre为前缀的字符串数量 */
	public static int prefixNumber(String s) {
        int p = 0;
        for(int i = 0; i < s.length(); i ++){
            int c = s.charAt(i) - 'a';
            if(nex[p][c] == 0) return 0;
            p = nex[p][c];
        }
        return pass[p];
	}

    /* 删除字符串 */
	public static void delete(String s) {
		if (find(s) > 0) {
			int p = 0;
			for (int i = 0; i < s.length(); i++) {
				int c = s.charAt(i) - 'a';
				if (--pass[nex[p][c]] == 0) {
					nex[p][c] = 0;
					return;
				}
				p = nex[p][c];
			}
			end[p]--;
		}
	}

    /* 清空trie */
	public static void clear() {
		for (int i = 0; i <= cnt; i++) {
			Arrays.fill(nex[i], 0);
			end[i] = 0;
			pass[i] = 0;
		}
	}
```