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

        System.out.println("outputA : " + Arrays.toString(productOfAllOtherElementsOne(inputA)));
        System.out.println("outputB : " + Arrays.toString(productOfAllOtherElementsOne(inputB)));

        System.out.println("outputA_1 : " + Arrays.toString(productOfAllOtherElementsTwo(inputA)));
        System.out.println("outputB_2 : " + Arrays.toString(productOfAllOtherElementsTwo(inputB)));

    }


    private static int[] productOfAllOtherElementsOne(int[] inputArray) {

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
    
    private static int[] productOfAllOtherElementsTwo(int[] inputArray) {

        int arrayLength = inputArray.length;

        
        int[] outputArray = new int[arrayLength];
        
        
        for (int i=0; i<arrayLength; i++) {


            // i번 만큼곱셈을 한다. 
            int prdLeft = inputArray[i];
            int prdRight = inputArray[i];

            int countA = 0;
            while (countA < i) {
                prdLeft *= inputArray[countA];
                countA++;
            }

            int countB = 0;
            while (countB < inputArray.length - i -1) {
                prdRight *= inputArray[inputArray.length - 1 - countB];
                countB++;
            }

            outputArray[i] = prdLeft * prdRight;
            

            
        }

        return outputArray;
    }

}