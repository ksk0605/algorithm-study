package stack.B6198;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {

    /*
    스택을 어떻게 활용할까?
    80000개 데이터 -> 최대 nlogn


    10, 3, 7, 4, 12, 2


             =
 =           =
 =     -     =
 =     =     =        -> 관리인이 보는 방향
 =  -  =  =  =
 =  =  =  =  =  =
10  3  7  4  12 2     -> 빌딩의 높이
[1][2][3][4][5][6]    -> 빌딩의 번호

12 2

10 3
     */
    public static void main(String... args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bf.readLine());

        int[] buildings = new int[n + 1];

        for (int i = 1; i <= n; i++) {
            buildings[i] = Integer.parseInt(bf.readLine());
        }

        if (n == 1) {
            System.out.println(0);
            return;
        }

        Stack<Integer> queue = new Stack<>();
        queue.add(buildings[1]);

        long count = 0; // 높이가 내림차순이 되도록 80000개의 빌딩이 서 있으면 count 값이 (79999 + 79998 + ... + 1) = 32억 정도 됩니다. count의 자료형을 unsigned int나 long long으로 해야 합니다.

        for (int i = 2; i <= n; i++) {
            int building = buildings[i];

            while (true) {
                if (queue.isEmpty() || queue.peek() > building) {
                    break;
                }
                queue.pop();
            }

            count += queue.size();
            queue.add(building);
        }

        System.out.println(count);
    }
}
