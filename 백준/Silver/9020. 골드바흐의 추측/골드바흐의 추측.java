import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class Main {
    static void solution() throws Exception {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        boolean[] primenumberArray = primeNumberCalculator();
        for (int i = 0; i < n; i++) {
            int targetNum = Integer.parseInt(br.readLine());
            int a = targetNum / 2;
            int b = targetNum / 2;
            while (true) {
                if (primenumberArray[a] == false && primenumberArray[b] == false) {
                    bw.write(a + " " + b + "\n");
                    break;
                }
                a--;
                b++;
        }
        }
        bw.flush();
        bw.close();
    }

    static boolean[] primeNumberCalculator() {
        ArrayList<Integer> primeNumberList = new ArrayList<Integer>();
        boolean[] primeNumberArray = new boolean[10001];
        primeNumberArray[0] = primeNumberArray[1] = true;
        for (int i = 2; i < primeNumberArray.length; i++) {
            for (int j = i * i; j < primeNumberArray.length; j += i) {
                if (primeNumberArray[j]) {
                    continue;
                }
                if (j % i == 0) {
                    primeNumberArray[j] = true;
                }
            }
        }
        for (int i = 0; i < primeNumberArray.length; i++) {
            if (!primeNumberArray[i]) {
                primeNumberList.add(i);
            }
        }
        return primeNumberArray;
    }

    public static void main(String[] args) throws Exception {
        solution();
    }
}