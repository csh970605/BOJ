import java.io.BufferedWriter;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class Main {
    public static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        ArrayList<Integer> rems = new ArrayList<Integer>();
        int n, rem;
        for (int i = 0; i < 10; i++) {
            n = Integer.parseInt(br.readLine());
            rem = n % 42;
            if (!rems.contains(rem)) {
                rems.add(rem);
            }
        }
        br.close();
        bw.write(String.valueOf(rems.size()));
        bw.flush();
        bw.close();
    }
    public static void main(String[] args) throws Exception {
        solution();
    }
}