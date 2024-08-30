import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;


public class Main {
    public static void solution() throws Exception {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] current_piece = new int[6];
        int[] correct_piece = new int[]{1, 1, 2, 2, 2, 8};
        for (int i = 0; i < current_piece.length; i++) {
            current_piece[i] = Integer.parseInt(st.nextToken());
            bw.write(correct_piece[i] - current_piece[i] + " ");
        }
        bw.flush();
        bw.close();
        br.close();
    }
    public static void main(String[] args) throws Exception {
        solution();
    }
}