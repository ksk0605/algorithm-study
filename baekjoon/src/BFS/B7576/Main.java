package BFS.B7576;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    public static void main(String... args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(bf.readLine());
        int m = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());

        int[][] box = new int[n + 2][m + 2];
        boolean[][] visited = new boolean[n + 2][m + 2];
        List<Tuple> starts = new ArrayList<>();

        for (int i = 0; i < n + 2; i++) {
            for (int j = 0; j < m + 2; j++) {
                box[i][j] = -22;
            }
        }

        for (int i = 1; i <= n; i++) {
            StringTokenizer line = new StringTokenizer(bf.readLine());
            for (int j = 1; j <= m; j++) {
                int tomato = Integer.parseInt(line.nextToken());
                if (tomato == 1) {
                    starts.add(new Tuple(i, j));
                }
                box[i][j] = tomato;
            }
        }
//        for (int i = 0; i < n + 2; i++) {
//            for (int j = 0; j < m + 2; j++) {
//                System.out.print(box[i][j] + " ");
//            }
//            System.out.println();
//        }

        bfs(starts, box, visited);

        int max = 0;
        for (int i = 0; i < n + 2; i++) {
            for (int j = 0; j < m + 2; j++) {
                if (box[i][j] == 0) {
                    System.out.println(-1);
                    return;
                }
                max = Math.max(box[i][j], max);
            }
        }
        System.out.println(max - 1);
    }

    private static void bfs(List<Tuple> starts, int[][] box, boolean[][] visited) {
        Tuple[] directions = {new Tuple(1, 0), new Tuple(-1, 0), new Tuple(0, 1), new Tuple(0, -1)};

        ArrayDeque<Tuple> deque = new ArrayDeque<>();
        for (int i = 0; i < starts.size(); i++) {
            deque.add(starts.get(i));
        }

        while (!deque.isEmpty()) {
            Tuple t = deque.poll();
            visited[t.x][t.y] = true;

            for (int j = 0; j < 4; j++) {
                int nextX = t.x + directions[j].x;
                int nextY = t.y + directions[j].y;

                if ((box[nextX][nextY] != -22 && box[nextX][nextY] != -1 && box[nextX][nextY] != 1) && !visited[nextX][nextY]) {
                    visited[nextX][nextY] = true;
                    box[nextX][nextY] = box[t.x][t.y] + 1;
                    deque.add(new Tuple(nextX, nextY));
                }
            }
        }

    }
}

class Tuple {

    int x;
    int y;

    Tuple(int x, int y) {
        this.x = x;
        this.y = y;
    }
}
