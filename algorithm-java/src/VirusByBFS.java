// NOT YET -> fix NPE

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class VirusByBFS {

    /**
     * from : https://www.acmicpc.net/problem/2606
     *
     * ※※※ Input ※※※
     * 첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다.
     * 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다.
     * 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.
     *
     * ex)
     * 7
     * 6
     * 1 2
     * 2 3
     * 1 5
     * 5 2
     * 5 6
     * 4 7
     *
     * ※※※ Output ※※※
     * 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.
     *
     * ex)
     * 4
     *
     */

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int nComputer = sc.nextInt();
        int nParedComputer = sc.nextInt();

        boolean[][] network = new boolean[nComputer+1][nComputer+1];
        boolean[] checkedComputer = new boolean[nParedComputer+1];

        // set true if there are any connections between computer
        for (int i = 0; i < nParedComputer; i++) {
            int m = sc.nextInt();
            int n = sc.nextInt();
            network[m][n] = true;
            network[n][m] = true;
        }

        Queue<Integer> checkingComputerQueue = new LinkedList<>();
        // add first computer
        checkingComputerQueue.add(1);
        checkedComputer[1] = true;


        while (!checkingComputerQueue.isEmpty()) {
            // get
            int computerN = checkingComputerQueue.remove();

            for (int i = 1; i <= nComputer; i++) {
                if (network[computerN][i] && !checkedComputer[i]) {
                    checkingComputerQueue.add(i);
                    checkedComputer[i] = true;
                }
            }
        }

        int nVirusComputer = 0;

        // start from 1; except first computer
        for (int i = 2; i <= nComputer; i++) {
            if (checkedComputer[i]) {
                nVirusComputer++;
            }
        }

        System.out.println(nVirusComputer);

    }
}