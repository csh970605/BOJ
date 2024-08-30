import java.io.BufferedWriter;
import java.io.BufferedReader;
import java.io.OutputStreamWriter;
import java.io.InputStreamReader;

public class Main {
    public static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int a = Integer.parseInt(br.readLine());
        String str = br.readLine();
        for (int i = 3; i > 0; i--) {
            bw.write((a*Integer.parseInt(str.substring(i-1,i)))+"\n");
        }
        bw.write((a * Integer.parseInt(str)) + "\n");
        bw.flush();
        bw.close();
        br.close();
    }
    public static void main(String[] args) throws Exception {
        solution();

    }
}