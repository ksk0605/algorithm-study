package greedy.B11000;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bf.readLine());


        ClassTime[] classTimes = new ClassTime[n];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(bf.readLine());

            String start = st.nextToken();
            String end = st.nextToken();
            ClassTime ct = new ClassTime(start, end);
            classTimes[i] = ct;
        }


        PriorityQueue<Integer> pq = new PriorityQueue<>();

        Arrays.sort(classTimes);
//        for (int i = 0; i < n; i++) {
//            System.out.println(classTimes[i].start + "  " + classTimes[i].end);
//        }
        pq.add(classTimes[0].end);
        for (int i = 1; i < n; i++) {
            ClassTime currCt = classTimes[i];
            if (pq.peek() <= currCt.start) {
                pq.poll();
            }
            pq.add(currCt.end);
        }

        System.out.println(pq.size());
    }
}
/*


 */

class ClassTime implements Comparable<ClassTime> {
    int start;
    int end;

    public ClassTime(String start, String end) {
        this.start = Integer.parseInt(start);
        this.end = Integer.parseInt(end);
    }

    @Override
    public int compareTo(ClassTime other) {
//        return Integer.compare(this.start, other.start);
        if (this.start != other.start) {
            return Integer.compare(this.start, other.start);
        } else {
            return Integer.compare(this.end, other.end);
        }
    }
}
