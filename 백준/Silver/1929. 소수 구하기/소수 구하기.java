import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    static void solution() throws Exception {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        br.close();
        int m = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        boolean[] primeNumbers = new boolean[n + 1];
        primeNumbers[0] = true;
        primeNumbers[1] = true;
        for (int i = 2; i < primeNumbers.length; i++) {
            if (primeNumbers[i]) {
                continue;
            }
            for (int j = i + i; j < primeNumbers.length; j += i) {
                primeNumbers[j] = true;
            }
        }
        for (int i = m; i <= n; i++) {
            if (!primeNumbers[i]) {
                bw.write(i + "\n");
            }
        }
        bw.flush();
        bw.close();
    }
    public static void main(String[] args) throws Exception {
        solution();
    }
}