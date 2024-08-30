import java.io.BufferedWriter;
import java.io.BufferedReader;
import java.io.OutputStreamWriter;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void solution() throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        int[] scores;
        StringTokenizer st;
        double cnt;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int num = Integer.parseInt(st.nextToken());
            double mean = 0;
            scores = new int[num];
            cnt = 0;
            for (int j = 0; j < num; j++) {
                scores[j] = Integer.parseInt(st.nextToken());
                mean += scores[j];
            }
            mean /= num;
            for (int j = 0; j < num; j++) {
                if (scores[j] > mean) {
                    cnt++;
                }
            }
            bw.write(String.format("%.3f", (cnt / num * 100)) + "%\n");
        }
        br.close();
        bw.flush();
        bw.close();
    }
    public static void main(String[] args) throws Exception {
        solution();
    }
}