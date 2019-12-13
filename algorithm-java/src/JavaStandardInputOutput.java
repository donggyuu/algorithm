import java.util.Scanner;

public class JavaStandardInputOutput {

    /**
     * 여러 문자열을 순차적으로 입력받아서 순차적으로 출력
     * refer to : https://limkydev.tistory.com/170
     *
     */

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int a, b;


        a = sc.nextInt();
        b = sc.nextInt();
        // 결과를 배열에 넣어서
        // foreach로 한번에 출력한다.

        System.out.println(a + " " + b);
    }

}
