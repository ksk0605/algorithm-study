package BFS.B2178;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;


public class Main {
    public static void main(String... args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(bf.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[][] maze = new int[n + 2][m + 2];
        boolean[][] visited = new boolean[n + 2][m + 2];

        for (int i = 0; i < n; i++) {
            String s = bf.readLine();
            char[] chars = s.toCharArray();
            for (int j = 0; j < m; j++) {
                int v = Integer.parseInt(String.valueOf(chars[j]));
                maze[i + 1][j + 1] = v;
            }
        }


        bfs(maze, visited);

//        for (int i = 0; i < n + 2; i++) {
//            for (int j = 0; j < m + 2; j++) {
//                System.out.print(maze[i][j] + " ");
//            }
//            System.out.println();
//        }

        System.out.println(maze[n][m]);
    }

    private static void bfs(int[][] maze, boolean[][] visited) {
        Tuple[] drs = {new Tuple(1, 0), new Tuple(-1, 0), new Tuple(0, 1), new Tuple(0, -1)};


        ArrayDeque<Tuple> dq = new ArrayDeque<>();
        dq.add(new Tuple(1, 1));

        while (!dq.isEmpty()) {
            Tuple t = dq.poll();

            for (int i = 0; i < 4; i++) {
                int nextX = t.x + drs[i].x;
                int nextY = t.y + drs[i].y;

                if (maze[nextX][nextY] == 1 && !visited[nextX][nextY]) {
                    dq.add(new Tuple(nextX, nextY));
                    visited[nextX][nextY] = true;
                    maze[nextX][nextY] += maze[t.x][t.y];
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
