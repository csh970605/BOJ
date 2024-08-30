import java.io.BufferedWriter;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            int bonus = 0;
            int score = 0;
            String result = br.readLine();
            for (int j = 0; j < result.length(); j++) {
                if (result.substring(j, j + 1).equals("O")) {
                    bonus++;
                    score += bonus;
                } else {
                    bonus = 0;
                }
            }
            bw.write(score + "\n");
        }
        br.close();
        bw.flush();
        bw.close();
    }
    public static void main(String[] args) throws Exception {
        solution();
    }
}