import java.io.BufferedWriter;
import java.io.OutputStreamWriter;

public class Main {
    public static void solution() throws Exception {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        boolean[] nums = new boolean[10000];
        nums[0] = true;
        int index;

        for (int i = 0; i < 10000; i++) {
            index = nself_num_counter(i + 1);
            if (index < 10000) {
                nums[index] = true;
            }
        }
        for (int i = 0; i < 10000; i++) {
            if (!nums[i]) {
                bw.write(i + "\n");
            }
        }
        bw.flush();
        bw.close();
    }

    public static int nself_num_counter(int num) {
        int sum = num;
        while (num != 0) {
            sum += num%10;
            num /= 10;
        }
        return sum;
    }

    public static void main(String[] args) throws Exception {
        solution();
    }
}