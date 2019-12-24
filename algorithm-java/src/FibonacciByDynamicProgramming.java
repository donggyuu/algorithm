public class FibonacciByDynamicProgramming {

    /**
     * get Fibonacci by Dynamic Programming
     * [1, 1, 2, 3, 5, 8 .....]
     *
     */

    // for dynamic fibonacci
    static int[] cached = new int[20]; // int[n], n => input value

    public static void main(String[] args) {

        // for normal fibonacci
        System.out.println("normal ways : " + normalFibonacci(5));

        // for dynamic fibonacci
        System.out.println("dynamic ways : " + dynamicFibonacci(5));

    }


    private static int normalFibonacci(int n) {

        if (n == 0) {
            return 1;
        } else if (n == 1) {
            return 1;
        } else {
            return normalFibonacci(n-1) + normalFibonacci(n-2);
        }
    }


    private static int dynamicFibonacci(int n) {

        if (n == 0 || n == 1) {
            return n;
        } else if (cached[n] != 0) {
            return cached[n];
        }

        cached[n] = dynamicFibonacci(n -2) + dynamicFibonacci(n-1);
        return cached[n];
    }

}
