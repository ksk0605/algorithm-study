package B15650;

import java.util.*;




import java.io.*;

public class B15650 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int a, b;
        StringTokenizer st = new StringTokenizer(br.readLine());
        a = Integer.parseInt(st.nextToken());
        b = Integer.parseInt(st.nextToken());
        bw.write(String.format("%d", a + b));
        // String s = "aa";
        // s.equals("bb");

        bw.flush();
    }
}
