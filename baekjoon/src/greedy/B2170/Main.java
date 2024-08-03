package greedy.B2170;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

    public static void main(String... args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bf.readLine());

        Tuple[] plusTp = new Tuple[n];
        Tuple[] minusTp = new Tuple[n];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(bf.readLine());
            Tuple tuple = new Tuple(Long.parseLong(st.nextToken()), Long.parseLong(st.nextToken()));
            plusTp[i] = tuple;
        }

        Arrays.sort(plusTp);
        PriorityQueue<Long> pq = new PriorityQueue<>(Collections.reverseOrder());

        long leng = plusTp[0].y - plusTp[0].x;
        pq.add(plusTp[0].y);

        for (int i = 1; i < n; i++) {
            Tuple curr = plusTp[i];
            leng += curr.y - curr.x;
            if (pq.peek() > curr.x) {
                leng -= pq.peek() - curr.x;
            }
            pq.add(curr.y);
//            System.out.println(leng);
        }

        System.out.println(leng);
    }
}

class Tuple implements Comparable<Tuple> {

    long x;
    long y;

    Tuple(long x, long y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public int compareTo(Tuple other) {
        if (x < other.x) {
            return -1;
        } else if (x == other.x && y < other.y) {
            return -1;
        } else if (x == other.x && y == other.y) {
            return 0;
        }
        return 1;
    }
}
