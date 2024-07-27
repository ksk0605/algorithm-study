package DP.B12852;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String... args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[] dp = new int[n + 1];
        int[] path = new int[n + 1];

        dp[1] = 0;

        for (int i = 2; i <= n; i++) {
            if (i % 3 == 0 && i % 2 == 0) {
                dp[i] = Math.min(Math.min(dp[i / 3], dp[i / 2]), dp[i - 1]) + 1;
                if (dp[i] == dp[i / 3] + 1) {
                    path[i] = i / 3;
                    continue;
                }
                if (dp[i] == dp[i / 2] + 1) {
                    path[i] = i / 2;
                    continue;
                }
                path[i] = i - 1;
                continue;
            }
            if (i % 3 == 0) {
                dp[i] = Math.min(dp[i / 3], dp[i - 1]) + 1;
                if (dp[i] == dp[i / 3] + 1) {
                    path[i] = i / 3;
                    continue;
                }
                path[i] = i - 1;
                continue;
            }
            if (i % 2 == 0) {
                dp[i] = Math.min(dp[i / 2], dp[i - 1]) + 1;
                if (dp[i] == dp[i / 2] + 1) {
                    path[i] = i / 2;
                    continue;
                }
                path[i] = i - 1;
                continue;
            }
            path[i] = i - 1;
            dp[i] = dp[i - 1] + 1;
        }
        System.out.println(dp[n]);

        int i = n;
        System.out.print(n);
        while (i != 1) {
            System.out.print(" " + path[i]);
            i = path[i];
        }
    }
}
