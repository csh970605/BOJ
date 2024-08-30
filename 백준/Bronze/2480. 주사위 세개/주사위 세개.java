import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    public static void solution() throws Exception {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        br.close();
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        if (a == b && b == c) {
            bw.write((10000 + a * 1000) + "\n");
        } else if (a == b && b != c) {
            bw.write((1000 + a * 100) + "\n");
        } else if (a == c && b != c) {
            bw.write((1000 + a * 100) + "\n");
        } else if (b == c && a != c) {
            bw.write((1000 + b * 100) + "\n");
        } else if (a != b && a != c && b != c) {
            int max = a;
            if (max < b) {
                if (b < c) {
                    max = c;
                } else {
                    max = b;
                }
            } else if (max < c) {
                if (c < b) {
                    max = b;
                } else {
                    max = c;
                }
            }
            bw.write((max * 100) + "\n");
        }
        bw.flush();
        bw.close();
    }

    public static void main(String[] args) throws Exception {
        solution();
    }
}