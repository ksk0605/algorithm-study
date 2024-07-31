package graph.B2606;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
    public static void main(String... args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bf.readLine());

        int[][] graph = new int[n + 1][n + 1];
        boolean[] visited = new boolean[n + 1];

        int ssang = Integer.parseInt(bf.readLine());

        for (int i = 0; i < ssang; i++) {
            StringTokenizer tokenizer = new StringTokenizer(bf.readLine());
            int from = Integer.parseInt(tokenizer.nextToken());
            int to = Integer.parseInt(tokenizer.nextToken());

            graph[from][to] = 1;
            graph[to][from] = 1;
        }

//        for (int i = 0; i <= n; i++) {
//            for (int j = 0; j < n + 1; j++) {
//                System.out.print(graph[i][j]);
//            }
//            System.out.println();
//        }

        int count = bfs(graph, visited);

        System.out.println(count);
    }

    public static int bfs(int[][] graph, boolean[] visited) {
        int start = 1;
        int count = 0;

        Deque<Integer> dq = new ArrayDeque<>();

        visited[1] = true;
        dq.add(start);

        while (!dq.isEmpty()) {
            Integer curr = dq.poll();

            for (int i = 1; i < graph[curr].length; i++) {
                if (graph[curr][i] == 1 && !visited[i]) {
                    dq.add(i);
                    count++;
                    visited[i] = true;
                }
            }
        }


        return count;
    }
}
