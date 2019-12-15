import com.sun.xml.internal.bind.v2.TODO;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class ShowMaxNumberInSlidingWindow {

    /**
     * Given a size W and a stream of number S. You can see only W numbers in the window.
     * Each time you receive a number from stream S then print max number in sliding window
     * <p>
     * ** input
     * *** ex. window size W=2 and number stream is S=[2,1,2,-1,3]
     * [W]    2
     * [N1]   2
     * [N2]   1
     * [N3]   2
     * [N4]  -1
     * [N5]   3
     * <p>
     * Where W is the number of the window size and Nn represents an element in the stream
     * <p>
     * ** output
     * After you read first W+1 lines, each time you read the number from the input, print max numbers in sliding window
     * [V1]   2
     * [V2]   2
     * [V3]   2
     * [V4]   3
     */

    // TODO : solve this -> when given stream number is int[]
    public static void main(String[] args) {

        List<Integer> window = new ArrayList<>();
        boolean isWindowSize = true;
        int windowSize= 0;

        int inputNum;
        int countPrintMax = 0;

        Scanner scanner = new Scanner(System.in);
        while (true) {

            // get number from console
            inputNum = scanner.nextInt();

            // 1st input number is window size
            if (isWindowSize) {
                windowSize = inputNum;

                isWindowSize = false;
                continue;
            }

            // set element in stream to window
            window.add(inputNum);

            // print max number from window
            if (windowSize <= countPrintMax) {
                // TODO : another way not using collections?
                System.out.println(Collections.max(window));
            }
            countPrintMax++;

        }
    }

}


