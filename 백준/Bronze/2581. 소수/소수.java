import java.io.BufferedWriter;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int m = Integer.parseInt(br.readLine());
        int n = Integer.parseInt(br.readLine());
        br.close();
        int minPrime = 0;
        int primeSum = 0;

        for (int i = m; i <= n; i++) {
            if (primeNumberChecker(i)) {
                if (primeSum == 0) {
                    minPrime = i;
                }
                primeSum += i;
            }
        }
        if (minPrime == 0) {
            bw.write("-1");
        } else {
            bw.write(primeSum + "\n" + minPrime);
        }
        bw.flush();
        bw.close();
    }

    public static boolean primeNumberChecker(int targetNumber) {
        if (targetNumber == 1) {
            return false;
        } else {
            for (int i = 2; i <= Math.sqrt(targetNumber); i++) {
                if (targetNumber % i == 0) {
                    return false;
                }
            }
        }
        return true;

    }

    public static void main(String[] args) throws Exception {
        solution();
    }
}