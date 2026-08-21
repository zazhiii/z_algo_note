import java.io.*;
import java.util.*;
public class Main {
// public class Main {

    public static void solve() throws IOException{
        

    }
    public static void main(String[] args) throws IOException {
        int T = 1;
        // T = rd.nextInt();
        while(T --> 0) solve();
        pw.flush();pw.close();
    }

    static Read rd = new Read();
    static PrintWriter pw = new PrintWriter(System.out);
    static int inf = (int)2e9;
    static long INF = (long)2e18; 
}

class Read{
    StringTokenizer st;
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String next() throws IOException{
        while (st == null || !st.hasMoreElements()) st = new StringTokenizer(br.readLine());
        return st.nextToken();
    }
    int nextInt() throws IOException {return Integer.parseInt(next());}
    long nextLong() throws IOException {return Long.parseLong(next());}
    double nextDouble() throws IOException {return Double.parseDouble(next());}
    String nextLine() throws IOException {return br.readLine();}
}