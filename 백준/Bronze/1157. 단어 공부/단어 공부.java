import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.InputStreamReader;

public class Main {
    static void solution() throws Exception {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] alphabet = new int[26];
        String str = br.readLine();
        char ch;
        int ascii;
        int index = 0;
        int max = 0;
        boolean check = false;
        br.close();

        for (int i = 0; i < alphabet.length; i++) {
            alphabet[i] = 0;
        }
        for (int i = 0; i < str.length(); i++) {
            ch = str.charAt(i);
            ascii = (int)ch;
            if (ascii < 97) {
                ascii += 32;
            }
            index = ascii - 97;
            alphabet[index]++;
        }
        for (int i = 0; i < alphabet.length; i++) {
            if (alphabet[i] > max) {
                max = alphabet[i];
                index = i;
                check = false;
            } else if (alphabet[i] == max) {
                check = true;
            }
        }
        if (check) {
            bw.write("?");
        } else {
            bw.write(String.valueOf((char) (index + 65)));
        }
        bw.flush();
        bw.close();
    }
    public static void main(String[] args) throws Exception {
        solution();
    }
}