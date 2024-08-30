import java.io.BufferedWriter;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int primeNums = 0;
        boolean check = false;
        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(st.nextToken());
            check = PrimeNumberChecker(num);
            if (check) {
                primeNums++;
            }
        }
        br.close();
        bw.write(String.valueOf(primeNums));
        bw.flush();
        bw.close();
    }

    static boolean PrimeNumberChecker(int num) {
        boolean check = true;

        if (num == 1) {
            check = false;
            return check;
        }

        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                check = false;
                return check;
            }
        }
        return check;
    }
    public static void main(String[] args) throws Exception {
        solution();
    }
}