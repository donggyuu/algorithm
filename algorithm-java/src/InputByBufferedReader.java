import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class InputByBufferedReader {

    /**
     * BufferedReader is faster than Scanner but need to IOException
     * - 코딩 테스트의 solution class에서 throws를 지원안해주면 못쓸듯
     * - 한번에 입력받고 출력 -> 입력&enter&입력 이런 식이면 Scanner
     */

    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String[] line = bf.readLine().split(" ");
        String a = line[0] + line[1];
        String b = line[2] + line[3];
        long ans = Long.valueOf(a) + Long.valueOf(b);
        System.out.println(ans);
    }

}