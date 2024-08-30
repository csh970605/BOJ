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
        int bud_year = Integer.parseInt(st.nextToken());
        String ad_year = String.valueOf(bud_year - 543);
        bw.write(ad_year);
        bw.flush();
        bw.close();
        br.close();
    }
    public static void main(String[] args) throws Exception {
        solution();
    }
}