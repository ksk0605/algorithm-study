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

        Tuple[] tps = new Tuple[n];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(bf.readLine());
            Tuple tuple = new Tuple(Long.parseLong(st.nextToken()), Long.parseLong(st.nextToken()));
            tps[i] = tuple;
        }

        Arrays.sort(tps);
        PriorityQueue<Long> pq = new PriorityQueue<>(Collections.reverseOrder());

        for (int i = 0; i < n; i++) {
            System.out.println(tps[i].x + " " + tps[i].y);
        }
        
        long leng = tps[0].y - tps[0].x;
        pq.add(tps[0].y);

        for (int i = 1; i < n; i++) {
            Tuple curr = tps[i];
            if (pq.peek() < curr.y) {
                leng += curr.y - curr.x;
                if (pq.peek() > curr.x) {
                    leng -= pq.peek() - curr.x;
                }
            }
            pq.add(curr.y);
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
