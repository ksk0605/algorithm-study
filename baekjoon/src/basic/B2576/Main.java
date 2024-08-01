package basic.B2576;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String... args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int[] nums = new int[7];
        for (int i = 0; i < 7; i++) {
            nums[i] = Integer.parseInt(bf.readLine());
        }

        Arrays.sort(nums);
        int sum = 0;
        boolean first = true;
        int low = 0;
        for (int i = 0; i < 7; i++) {
            if (nums[i] % 2 != 0) {
                if (first) {
                    low = nums[i];
                    first = false;
                }
                sum += nums[i];
            }
        }
        if (first) {
            System.out.println(-1);
            return;
        }
        System.out.println(sum);
        System.out.println(low);
    }
}
