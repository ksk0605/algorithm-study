package ses9928.B1522;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String... args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String abs = bf.readLine();

        String circle = abs + abs;

        // 서로 다른 b 사이의 거리가 가장 짧은
        char[] absCharArray = abs.toCharArray();
        int aCount = getcount(absCharArray, 'a');

        int start = 0;
        int end = aCount - 1;
        int count = 1000000;

        for (int i = 0; i < abs.length(); i++) {
//            System.out.println(start);
//            System.out.println(end);

            int bCount = 0;
            for (int j = start; j <= end; j++) {
                if (circle.charAt(j) == 'b') {
                    bCount++;
                }

            }
//            System.out.println(bCount);
            count = Math.min(count, bCount);
            start++;
            end++;
        }
        System.out.println(count);
    }

    public static int getcount(char[] chars, char c) {
        int count = 0;
        for (int i = 0; i < chars.length; i++) {
            if (chars[i] == c) {
                count++;
            }
        }
        return count;
    }
}
