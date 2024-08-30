import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static int[] nums;
    public static int[] sorted_nums;
    public static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        nums = new int[n];
        sorted_nums = new int[nums.length];
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(br.readLine());
        }
        br.close();
        mergeSort(0, nums.length - 1);
        for (int i = 0; i < nums.length; i++) {
            bw.write(nums[i] + "\n");
        }
        bw.flush();
        bw.close();
    }

    public static void mergeSort(int start, int end) {
        if (start < end) {
            int mid = (start + end) / 2;
            int left = start;
            int right = mid + 1;
            mergeSort(left, mid);
            mergeSort(right, end);
            int index = left;
            while (left <= mid || right <= end) {
                if (right > end || (left <= mid && nums[left] <= nums[right])) {
                    sorted_nums[index] = nums[left];
                    index++;
                    left++;
                } else {
                    sorted_nums[index] = nums[right];
                    index++;
                    right++;
                }
            }
            for (int i = start; i <= end; i++) {
                nums[i] = sorted_nums[i];
            }
        }
    }

    public static void main(String[] args) throws Exception {
        solution();
    }
}