import java.io.BufferedWriter;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    public static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int cook = Integer.parseInt(br.readLine());
        br.close();
        int h = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int cook_h = cook / 60;
        int cook_m = cook % 60;
        int h_count = h+cook_h;
        int m_count = m+cook_m;
        bw.write((m_count >= 60) ? ((h_count + 1) >= 24 ? ((h_count - 23) + " " + (m_count - 60)) : ((h_count + 1) + " " + (m_count - 60))) : (h_count >= 24 ? ((h_count - 24) + " " + (m_count)) : (h_count + " " + (m_count))));
        bw.flush();
        bw.close();
    }
    public static void main(String[] args) throws Exception {
        solution();
    }
}