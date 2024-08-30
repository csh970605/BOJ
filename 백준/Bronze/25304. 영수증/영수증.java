import java.io.BufferedWriter;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    public static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        int sum = 0;
        int price, num;
        int amount = Integer.parseInt(br.readLine());
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            price = Integer.parseInt(st.nextToken());
            num = Integer.parseInt(st.nextToken());
            sum = sum + num * price;
        }
        bw.write(sum == amount ? "Yes" : "No");
        bw.flush();
        bw.close();
    }
    public static void main(String[] args) throws Exception {
        solution();
    }

}