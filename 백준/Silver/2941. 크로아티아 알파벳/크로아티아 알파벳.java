import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {
    static void solution() throws Exception {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<String> arrayList = new ArrayList<>(Arrays.asList("c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="));
        String str = br.readLine();
        br.close();
        String conStr;
        int wordNum = 0;
        for (int i = 0; i < str.length(); i++) {
            if (i < str.length() - 2) {
                conStr = str.substring(i, i + 3);
                if (arrayList.contains(conStr)) {
                    i += 2;
                    wordNum++;
                } else {
                    conStr = str.substring(i, i + 2);
                    if (arrayList.contains(conStr)) {
                        i++;
                        wordNum++;
                    } else {
                        conStr = str.substring(i, i + 1);
                        wordNum++;
                    }
                }
            } else if (i < str.length() - 1) {
                conStr = str.substring(i, i + 2);
                if (arrayList.contains(conStr)) {
                    i++;
                    wordNum++;
                } else {
                    conStr = str.substring(i, i + 1);
                    wordNum++;
                }
            } else {
                conStr = str.substring(i, i + 1);
                wordNum++;
            }
        }
        bw.write(String.valueOf(wordNum));
        bw.flush();
        bw.close();
    }
    public static void main(String[] args) throws Exception {
        solution();
    }
}