import java.io.BufferedWriter;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    public static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        br.close();
        int[] num = new int[n];
        int min = 0;
        int max = 0;
        for (int i = 0; i < n; i++) {
            num[i] = Integer.parseInt(st.nextToken());
            if (i == 0) {
                min = num[i];
                max = num[i];
            }
            if (num[i] <= min) {
                min = num[i];
            }
            if (num[i] >= max) {
                max = num[i];
            }
        }
        bw.write(min + " " + max);
        bw.flush();
        bw.close();
    }
    public static void main(String[] args) throws Exception {
        solution();
    }
}