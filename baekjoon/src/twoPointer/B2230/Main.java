package twoPointer.B2230;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    /*
    {1, 2, 3, 4, 5}
    M=3
    1 4
    2 5

    배열의 개수가 100,000 -> nlogn 이하로 풀어야 함. 정렬, 해쉬, 이분탐색, 우선순위 큐 등
    한번의 반복으로


    배열 정렬

    for (n의 개수만큼)
        if (값 차이 == M) {
            M 출력 하고 리턴
        }
        if (b포인터가 가리키는 값 - a포인터가 가리키는 값 > M)
             Min(현재 차이 값, 차이값)
             a포인터 위치 이동
        else
             b포인터 위치 이동
     */
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer stringTokenizer = new StringTokenizer(bf.readLine());

        int n = Integer.parseInt(stringTokenizer.nextToken());
        int m = Integer.parseInt(stringTokenizer.nextToken());

        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(bf.readLine());
        }

        Arrays.sort(nums);

        int rowP = 0;
        int highP = 0;
        int minDiff = 2000000001;

        while (rowP < nums.length && highP < nums.length) {
            int row = nums[rowP];
            int high = nums[highP];

            int diff = high - row;

            if (diff == m) {
                System.out.println(m);
                return;
            }
            if (diff > m) {
                minDiff = Math.min(minDiff, diff);
                rowP++;
            } else {
                highP++;
            }
        }

        System.out.println(minDiff);
    }
}
