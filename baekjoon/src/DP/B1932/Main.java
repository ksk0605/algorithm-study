package DP.B1932;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String... args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());

        int[][] dp = new int[n + 1][n + 2];

        /*
        dp[i][j] += Max(dp[i-1]dp[j],dp[i-1][j-1])
         */
        for (int i = 1; i <= n; i++) {
            StringTokenizer st = new StringTokenizer(bf.readLine());
            for (int j = 1; j <= i; j++) {
                dp[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 2; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                dp[i][j] += Math.max(dp[i - 1][j], dp[i - 1][j - 1]);
            }
        }

        int max = 0;
        for (int j = 1; j <= n; j++) {
            max = Math.max(max, dp[n][j]);
        }

        System.out.println(max);
    }
}
