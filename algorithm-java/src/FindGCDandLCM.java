public class FindGCDandLCM {

    public static void main(String[] args) {

        for (int i : findGCDandLCM(10, 2)) {
            System.out.println(i);
        }

    }

    /**
     * n, m 의 최대공약수, 최소공배수를 구하기
     * int[0] : 최대공약수, int[1] : 최소공배수
     */
    public static int[] findGCDandLCM(int n, int m) {
        int[] result = new int[2];

        /*
        입력값 대소구분
         */
        int big;
        int small;

        if (n > m) {
            big = n;
            small = m;
        } else {
            big = m;
            small = n;
        }

        result[0] = gcd(big, small);
        result[1] = big*small/result[0];

        return result;
    }

    /**
     * 유클리드 호제법으로 최대공약수 구하기
     */
    public static int gcd(int n, int m) {
        if (n % m == 0) {
            return m;
        }

        return gcd(m, n%m);
    }
}
