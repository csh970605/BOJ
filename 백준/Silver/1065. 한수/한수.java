import java.io.OutputStreamWriter;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.BufferedReader;

public class Main {
    public static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        br.close();
        int cnt = 0;
        boolean[] nums = new boolean[n + 1];
        nums = arithmetic_checker(nums);
        for (int i = 1; i < nums.length; i++) {
            if (nums[i]) {
                cnt++;
            }
        }
        bw.write(String.valueOf(cnt));
        bw.flush();
        bw.close();
    }

    public static boolean[] arithmetic_checker(boolean[] nums) {
        int hundreds, tens, units;
        for (int i = 1; i < nums.length; i++) {
            if (i < 100) {
                nums[i] = true;
            } else {
                hundreds = i / 100;
                tens = (i - hundreds*100) / 10;
                units = (i - hundreds*100 - tens*10) % 10;
                if ((hundreds - tens) == (tens - units)) {
                    nums[i] = true;
                }
            }
        }
        return nums;
    }
    public static void main(String[] args) throws Exception {
        solution();
    }
}