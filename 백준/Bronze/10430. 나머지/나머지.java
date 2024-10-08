import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    public static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int result = (a+b)%c;
        bw.write(result + "\n");
        result = ((a%c) + (b%c))%c;
        bw.write(result + "\n");
        result = ((a*b)%c);
        bw.write(result + "\n");
        result = ((a%c)*(b%c))%c;
        bw.write(result + "\n");
        bw.flush();
        bw.close();
        br.close();
    }
    public static void main(String[] args) throws Exception {
        solution();
    }
}