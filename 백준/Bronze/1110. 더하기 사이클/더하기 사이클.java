import java.io.BufferedWriter;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int num = Integer.parseInt(br.readLine());
        int a = num / 10;
        int b = num % 10;
        int cnt = 0;
        int temp = 0;
        br.close();
        while (true) {
            cnt++;
            temp = a;
            a = b;
            b = (temp + b) % 10;
            if (a * 10 + b == num) {
                bw.write(String.valueOf(cnt));
                break;
            }
        }
        bw.flush();
        bw.close();
    }
    public static void main(String[] args) throws Exception {
        solution();
    }
}