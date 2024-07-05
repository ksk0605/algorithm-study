package B1000;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        // 자바 환경의 코딩테스트의 입출력에서는 BufferedReader 와 StringTokenizer 를 사용하는 것이 좋다.
//        Scanner이나 System.in.read를 사용하는 것이 일반적이나, 코딩테스트용으로 빠르게 입력받기 위해서는 BufferedReader을 사용하며,
//        StringTokenizer은 공백이 있는 경우 문자열이 공백처리를 땡겨 채우도록 하여 BufferedReader보다 더 빠르다고 한다.
//        BufferedReader, InputStreamReader은 java.io에 속하고 StringTokenizer은 java.util에 속한다.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stk = new StringTokenizer(br.readLine()," ");

        int n = Integer.parseInt(stk.nextToken());
        int m = Integer.parseInt(stk.nextToken());

        System.out.println(n+m);
    }
}
