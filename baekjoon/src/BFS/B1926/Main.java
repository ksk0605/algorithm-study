package BFS.B1926;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Objects;
import java.util.Queue;
import java.util.StringTokenizer;


public class Main {

    public static Node[] dists = new Node[]{new Node(1, 0), new Node(-1, 0), new Node(0, 1),
        new Node(0, -1)};


    public static void main(String... args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n, m;
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        int[][] graph = new int[n + 2][m + 2];

        for (int i = 1; i <= n; i++) {
            String line = br.readLine();
            st = new StringTokenizer(line);
            for (int j = 1; j <= m; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

//        for (int i = 0; i < n + 2; i++) {
//            for (int j = 0; j < m + 2; j++) {
//                System.out.print(graph[i][j] + " ");
//            }
//            System.out.println();
//        }
        boolean[][] visited = new boolean[n + 2][m + 2];

        int count = 0;
        int area = 0;

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (!visited[i][j] && graph[i][j] == 1) {
                    int a = bfs(new Node(i, j), graph, visited);
                    count++;
                    area = Math.max(area, a);
                }
            }
        }

        System.out.println(count);
        System.out.println(area);
    }

    private static int bfs(Node start, int[][] graph, boolean[][] visited) {
        Queue<Node> q = new LinkedList<>();
        q.add(start);
        visited[start.x][start.y] = true;

        int area = 1;

        while (!q.isEmpty()) {
            Node curr = q.poll();
            for (int i = 0; i < 4; i++) {
                Node dist = dists[i];
                if (graph[curr.x + dist.x][curr.y + dist.y] == 1 && !visited[curr.x + dist.x][curr.y
                    + dist.y]) {
                    q.add(new Node(curr.x + dist.x, curr.y + dist.y));
                    visited[curr.x + dist.x][curr.y + dist.y] = true;
                    area += 1;
                }
            }
        }

//        for (int i = 0; i < 8; i++) {
//            for (int j = 0; j < 7; j++) {
//                System.out.print(visited[i][j] + " ");
//            }
//            System.out.println();
//        }
        return area;
    }
}


class Node {

    int x;
    int y;

    public Node(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        Node node = (Node) o;
        return x == node.x && y == node.y;
    }

    @Override
    public int hashCode() {
        return Objects.hash(x, y);
    }
}
