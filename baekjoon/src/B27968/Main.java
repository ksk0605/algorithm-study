package B27968;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
    public static void main(String... args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(bf.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(bf.readLine());

        long[] candies = new long[m];
        candies[0] = Integer.parseInt(st.nextToken());

        for (int i = 1; i < m; i++) {
            long candy = Long.parseLong(st.nextToken());
            candies[i] = candies[i - 1] + candy;
        }

//        for (int i = 0; i < m; i++) {
//            System.out.println(candies[i]);
//        }

        Tuple[] wantList = new Tuple[n];
        String[] results = new String[n];

        for (int i = 0; i < n; i++) {
            long wants = Long.parseLong(bf.readLine());
            wantList[i] = new Tuple(i, wants);
        }

        Arrays.sort(wantList, Collections.reverseOrder());

        for (int i = 0; i < n; i++) {
            System.out.println(wantList[i].value);
        }

        int candiesIndex = 0;
        int wantsIndex = 0;

        while (wantsIndex < wantList.length) {
            if (candiesIndex == candies.length - 1 && wantList[wantsIndex].value > candies[candiesIndex]) {
                results[wantList[wantsIndex].index] = "Go away!";
                wantsIndex++;
                continue;
            }
            if (candies[candiesIndex] >= wantList[wantsIndex].value) {
                results[wantList[wantsIndex].index] = String.valueOf(candiesIndex + 1);
                wantsIndex++;
            } else {
                if (candiesIndex < candies.length) {
                    candiesIndex++;
                }
            }
        }

        for (int i = 0; i < n; i++) {
            System.out.println(results[i]);
        }
    }
}

class Tuple implements Comparable<Tuple> {
    int index;
    long value;

    Tuple(int index, long value) {
        this.index = index;
        this.value = value;
    }

    @Override
    public int compareTo(Tuple o) {
        if (this.value < o.value) {
            return 1;
        } else if (value > o.value) {
            return -1;
        }
        return 0;
    }
}