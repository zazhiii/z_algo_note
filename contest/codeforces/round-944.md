# Round 944 (Div. 4)（exc：G）

[Problem - D - Codeforces](https://codeforces.com/contest/1971/problem/D)

```java
import java.io.*;
import java.util.*;
public class Main {
	static Scanner sc = new Scanner(System.in);
	static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

	static int T;
	public static void main(String[] args) throws IOException{
		T = sc.nextInt();
		while( T --> 0 ) {
			char[] s = sc.next().toCharArray();
			boolean f = false;
			int cnt = 0;
			for(int i = 0; i<s.length - 1; i++) {
				if(s[i] != s[i + 1]) cnt ++;
				if(s[i] == '0' && s[i + 1] == '1') f = true;
			}
			pw.println(f ? cnt:cnt + 1);
		}
		pw.flush();
	}
}

```

[Problem - E - Codeforces](https://codeforces.com/contest/1971/problem/E)

```java
package algorithm;

import java.io.*;
import java.util.*;
public class Main {
	static Scanner sc = new Scanner(System.in);
	static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
	static Read rd = new Read();
	static int T, n, k, q, a[], b[], d;
	static double eps = 0.000000000000000000000000000000000000000000000000000;
	public static void main(String[] args) throws IOException{
		T = rd.nextInt();
		while( T --> 0 ) {
			n = rd.nextInt();
			k = rd.nextInt();
			q = rd.nextInt();
			a = new int[k + 1];
			b = new int[k + 1];
			for(int i = 1; i<=k; i++) a[i] = rd.nextInt();
			for(int j = 1; j<=k; j++) b[j] = rd.nextInt();
			
			while(q --> 0) {
				long ans = 0;
				d = rd.nextInt();
				int l = 0, r = k, i = 0;
				while(l <= r) {
					int m = (l + r) >>> 1;
					if(a[m] <= d) {
						i = m;
						l = m + 1;
					}else {
						r = m - 1;
					}
				}
				ans = b[i];
				if(i != k) {
                    //坑死了。。
					pw.print((ans + 1l * (d - a[i] ) * (b[i + 1] - b[i]) / (a[i + 1] - a[i]) )+ " ");
				}else {
					pw.print(ans + " ");
				}
				
			}
			pw.println();
		}
		pw.flush();
	}
}
class Read{
	StreamTokenizer st = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
	public int nextInt() throws IOException{
		st.nextToken();
		return (int)st.nval;
	}
}
```

[F - Circle Perimeter](https://codeforces.com/contest/1971/problem/F)

> 二分

[G. XOUR](https://codeforces.com/contest/1971/problem/G)

给出$n$个数的数组$a$，当$a_i\oplus a_j<4$时可以交换二者，输出交换后最小字典序的数组。

> 观察出要满足$a \oplus b < 4$，则$a,b$的二进制位从第三位往上必须相同。满足这些这些高位一样的所有数都可以交换，我们这些高位相同的数视作一个组，在数组中排序即可，哈希表加优先队列记录所有组的数，在输出时$i$位置的数应该是和$a_i$同组的数，输出这一组中最小的数在这个位置即可（优先队列poll出）。

```java
    static public void solve() throws IOException{
        int n = rd.nextInt();
        int a[] = new int[n];
        for(int i = 0; i < n; i ++) a[i] = rd.nextInt();
        Map<Integer, Queue<Integer>> map = new HashMap<>();
        for(int i = 0; i < n; i ++){
            int x = a[i];
            if(!map.containsKey(x >> 2)) map.put(x >> 2, new PriorityQueue<>());
            map.get(x >> 2).add(x);
        }
        for(int i = 0; i < n; i ++) pw.print(map.get(a[i] >> 2).poll() + " ");
        pw.print( "\n");
    }
```

