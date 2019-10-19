import java.util.Arrays;

public class ProductOfAllOtherElements {

    /* 
     * 배열이 주어질 때, 아래를 만족하는 새로운 배열을 만드는 함수를 만들어라.
     * --> 새로운 배열 : i번째 원소는, i번째를 제외한 다른 원소들의 곱이 온다.
     * 
     * ex) input: [1, 2, 3, 4, 5]  output: [120, 60, 40, 30, 24]
     *     input: [3, 2, 1]        output: [2, 3, 6]
     */

    public static void main(String[] args) {

        int[] inputA = {1, 2, 3, 4, 5};
        int[] inputB = {3, 2, 1};

        System.out.println("outputA-using devide : " + Arrays.toString(productOfElementsUsingDevide(inputA)));
        System.out.println("outputB-using devide : " + Arrays.toString(productOfElementsUsingDevide(inputB)));

        System.out.println("outputA_using product : " + Arrays.toString(productOfElementsUsingProduct(inputA)));
        System.out.println("outputB_using product : " + Arrays.toString(productOfElementsUsingProduct(inputB)));
    }


    /*
     * get all product of elements then divide with inputArray[i]
     */
    private static int[] productOfElementsUsingDevide(int[] inputArray) {

        // get length of array
        int arrayLength = inputArray.length;

        // get product of all elements
        int prdAllElements = 1;
        for (int i=0; i<arrayLength; i++) {
            prdAllElements *= inputArray[i];
        }

        // make output array
        int[] outputArray = new int[arrayLength];
        for (int i=0; i<arrayLength; i++) {
            outputArray[i] = prdAllElements / inputArray[i];
        }

        return outputArray;
    }


    /*
     * 1. get elements before inputArray[i]
     * 2. get elements after inputArray[i]
     * 3. product before&after elements
     */
    private static int[] productOfElementsUsingProduct(int[] inputArray) {

        // get length of array
        int arrayLength = inputArray.length;

        int[] outputArray = new int[arrayLength];

        for (int i=0; i<arrayLength; i++) {

            // set initial value 
            int prdLeft = 1;
            int prdRight = 1;

            // get product of left value
            // ex. for getting outputArray[2] then get product of inputArray[0], inputArray[1]
            int countFlgA = 0;
            while (countFlgA < i) {
                prdLeft *= inputArray[countFlgA];

                countFlgA++;
            }

            // get product of right value
            // ex. for getting outputArray[2] then get product of inputArray[3], inputArray[4]...
            int countFlgB = 0;
            while (countFlgB < inputArray.length - i -1) {
                prdRight *= inputArray[inputArray.length- countFlgB -1];

                countFlgB++;
            }

            outputArray[i] = prdLeft * prdRight;
        }

        return outputArray;
    }

}