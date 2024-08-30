import java.io.BufferedWriter;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class Main {
    public static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int line = Integer.parseInt(br.readLine());
        ArrayList<Integer> arr = new ArrayList<Integer>();
        for (int i = 0; i < line; i++) {
            int n = Integer.parseInt(br.readLine());
            if (arr.size() == 0) {
                arr.add(n);
            } else {
                for (int j = 0; j < arr.size(); j++) {
                    if (n < arr.get(j)) {
                        arr.add(j, n);
                        break;
                    } else if (j == arr.size() - 1) {
                        arr.add(n);
                        break;
                    }
                }
            }
        }
        br.close();
        for (int i = 0; i < arr.size(); i++) {
            bw.write(arr.get(i) + " \n");
        }
        bw.flush();
        bw.close();
    }
    public static void main(String[] args) throws Exception {
        solution();
    }
}