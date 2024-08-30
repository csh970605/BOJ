import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    static void solution() throws Exception {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuffer str1, str2;
        int n1, n2;

        StringTokenizer st = new StringTokenizer(br.readLine());
        br.close();
        str1 = new StringBuffer(st.nextToken()).reverse();
        str2 = new StringBuffer(st.nextToken()).reverse();

        n1 = Integer.parseInt(str1.toString());
        n2 = Integer.parseInt(str2.toString());

        if (n1 > n2) {
            bw.write(String.valueOf(n1));
        } else {
            bw.write(String.valueOf(n2));
        }
        bw.flush();
        bw.close();
    }

    public static void main(String[] args) throws Exception {
        solution();
    }
}