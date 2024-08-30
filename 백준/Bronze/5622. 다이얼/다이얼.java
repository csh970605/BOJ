import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    static void solution() throws Exception {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int sum = 0;
        int n;

        String str = br.readLine();
        br.close();

        for (int i = 0; i < str.length(); i++) {
            n = (int) str.charAt(i);
            if (n <= 67) {
                sum += 3;
            } else if (n <= 70) {
                sum += 4;
            } else if (n <= 73) {
                sum += 5;
            } else if (n <= 76) {
                sum += 6;
            } else if (n <= 79) {
                sum += 7;
            } else if (n <= 83) {
                sum += 8;
            } else if (n <= 86) {
                sum += 9;
            } else {
                sum += 10;
            }
        }
        bw.write(String.valueOf(sum));
        bw.flush();
        bw.close();
    }
    public static void main(String[] args) throws Exception {
        solution();
    }
}