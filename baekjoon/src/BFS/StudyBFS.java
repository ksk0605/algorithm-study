package BFS;

import java.util.LinkedList;
import java.util.Queue;

public class StudyBFS {

    public static void main(String... args) {
        // 2차원 배열로 그래프 저장
        // 1번 노드부터 사용하기 위해 0번 노드는 빈 값으로 초기화
        int[][] graph = {{}, {2, 3, 8}, {1, 6, 8}, {1, 5}, {5, 7}, {3, 4, 7}, {2}, {4, 5}, {1, 2}};

        // default 값인 false 로 저장
        boolean[] visited = new boolean[9];

        String path = bfs(graph, visited, 1);

        System.out.println(path);
    }

    public static String bfs(int[][] graph, boolean[] visited, int start) {
        Queue<Integer> q = new LinkedList<Integer>();

        q.offer(start);

        visited[start] = true;

        StringBuilder path = new StringBuilder();

        while (!q.isEmpty()) {
            Integer curr = q.remove();
            path.append(curr).append(" ");

            for (int i = 0; i < graph[curr].length; i++) {
                if (visited[graph[curr][i]]) {
                    continue;
                }

                q.offer(graph[curr][i]);
                visited[graph[curr][i]] = true;
            }
        }

        return path.toString();
    }
}
