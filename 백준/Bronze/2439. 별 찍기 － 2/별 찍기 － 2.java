import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void solution() throws Exception {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        br.close();
        for (int i = 1; i <= n; i++) {
            for (int j = n; j - i > 0; j--) {
                bw.write(" ");
            }
            for (int j = 0; j < i; j++) {
                bw.write("*");
            }
            bw.write("\n");
        }
        bw.flush();
        bw.close();
    }

    public static void main(String[] args) throws Exception {
        solution();
    }
}