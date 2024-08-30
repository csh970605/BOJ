import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    static void solution() throws Exception {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str;
        int gNum = 0;
        boolean checker;
        int index;
        char ch;

        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            str = br.readLine();
            checker = true;
            for (int j = 0; j < str.length(); j++) {
                ch = str.charAt(j);
                index = j;
                for (int k = j + 1; k < str.length(); k++) {
                    if (ch == str.charAt(k)) {
                        if ((k - index) != 1) {
                            checker = false;
                            break;
                        } else {
                            index = k;
                        }
                    }
                }
                if (!checker) {
                    break;
                }
            }
            if (checker) {
                gNum++;
            }
        }
        br.close();
        bw.write(String.valueOf(gNum));
        bw.flush();
        bw.close();
    }
    public static void main(String[] args) throws Exception {
        solution();
    }
}