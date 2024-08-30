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
        double max = 0;
        double score;
        double[] scores = new double[n];
        double score_sum = 0;
        for (int i = 0; i < n; i++) {
            score = Double.parseDouble(st.nextToken());
            scores[i] = score;
            if (max < score) {
                max = score;
            }
            //max = Math.max(max, score);
        }
        for (int i = 0; i < n; i++) {
            scores[i] = scores[i]/max*100;
            score_sum += scores[i];
        }
        br.close();
        bw.write(String.valueOf((score_sum / n)));
        bw.flush();
        bw.close();
    }
    public static void main(String[] args) throws Exception {
        solution();
    }
}