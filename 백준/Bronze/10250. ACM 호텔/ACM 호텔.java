import java.io.BufferedWriter;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    static void solution()throws Exception {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int h, w, n, floor, seq;
        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            st = new StringTokenizer(br.readLine());
            h = Integer.parseInt(st.nextToken());
            w = Integer.parseInt(st.nextToken());
            n = Integer.parseInt(st.nextToken());
            seq = n / h;
            floor = n % h;
            if (floor == 0) {
                floor = h;
            } else {
                seq++;
            }
            bw.write((floor * 100 + seq) + "\n");
        }
        br.close();
        bw.flush();
        bw.close();
    }
    public static void main(String[] args) throws Exception {
        solution();
    }
}