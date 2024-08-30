import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class Main {
    static void solution() throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BigInteger a, b;
        StringTokenizer st = new StringTokenizer(br.readLine());
        br.close();
        a = new BigInteger(st.nextToken());
        b = new BigInteger(st.nextToken());
        bw.write(String.valueOf(a.add(b)));
        bw.flush();
        bw.close();
    }
    public static void main(String[] args) throws Exception {
        solution();
    }
}