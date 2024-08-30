import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    static void solution() throws Exception {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        int k, n;
        int[][] apt = new int[15][15];
        for (int i = 0; i < 15; i++) {
            apt[i][0] = 1;
            apt[0][i] = i + 1;
        }
        for (int i = 1; i < 15; i++) {
            for (int j = 1; j < 15; j++) {
                apt[i][j] = apt[i][j - 1] + apt[i - 1][j];
            }
        }
        for (int i = 0; i < t; i++) {
            k = Integer.parseInt(br.readLine());
            n = Integer.parseInt(br.readLine()) - 1;
            bw.write(apt[k][n] + "\n");
        }
        bw.flush();
        bw.close();
        br.close();
    }
    public static void main(String[] args) throws Exception {
        solution();
    }
}