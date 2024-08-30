import java.io.BufferedWriter;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String str = br.readLine();
        char c;
        int index;
        br.close();
        int[] alphabet = new int[26];
        for (int i = 0; i < alphabet.length; i++) {
            alphabet[i] = -1;
        }
        for (int i = 0; i < str.length(); i++) {
            c = str.charAt(i);
            index = (int)c - 97;
            if (alphabet[index] == -1) {
                alphabet[index] = i;
            }
        }
        for (int i = 0; i < alphabet.length; i++) {
            bw.write(alphabet[i] + " ");
        }
        bw.flush();
        bw.close();
    }
    public static void main(String[] args) throws Exception {
        solution();
    }
}