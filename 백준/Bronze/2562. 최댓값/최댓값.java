import java.io.BufferedWriter;
import java.io.BufferedReader;
import java.io.OutputStreamWriter;
import java.io.InputStreamReader;

public class Main {
    public static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int[] n = new int[9];
        int max = 0;
        int cnt = 1;
        for (int i = 0; i < 9; i++) {
            n[i] = Integer.parseInt(br.readLine());
            if (i == 0) {
                max = n[i];
            }
            if (max < n[i]) {
                max = n[i];
                cnt = i + 1;
            }
        }
        br.close();
        bw.write(max + "\n" + cnt);
        bw.flush();
        bw.close();
    }
    public static void main(String[] args) throws Exception {
        solution();
    }
}