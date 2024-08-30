import java.io.BufferedWriter;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        double doubleN = Double.parseDouble(br.readLine());
        br.close();
        int intN = (int) (1 + Math.sqrt(8 * doubleN - 3)) / 2;
        int temp = intN;
        int firstNum = (intN * intN - intN + 2) / 2;
        int numerator, denominator;
        numerator = intN - (int) doubleN + firstNum;
        denominator = (int) doubleN - firstNum + 1;
        if (intN % 2 == 1) {
            bw.write(String.valueOf(numerator + "/" + denominator));
        } else {
            bw.write(String.valueOf(denominator + "/" + numerator));
        }
        bw.flush();
        bw.close();
    }
    public static void main(String[] args) throws Exception {
        solution();
    }
}