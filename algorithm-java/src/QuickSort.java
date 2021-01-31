public class QuickSort {

    public static void main(String[] args) {

        int data[] = {66, 10, 1, 34, 5, -10};

        quickSort(data, 0, data.length - 1);

        // print
        for(int i=0; i<data.length; i++){
            System.out.print(data[i] + " ");
        }

    }

    /*
    메디안 퀵 정렬
    언제 최악이 되는가? pivot에 따라, 나머지 값이 완전히 정렬되어 있는 경우다.
    왜? -> 비교를 하는 것에 n, 그걸 재귀를 돌리니까 또 n -> n2의 복잡도.
    고로, 중앙값으로 pivot을 설정하면 nlogN 의 복잡도.
     */
    public static void quickSort(int[] data, int L, int R) {
        int left = L;
        int right = R;
        int pivot = data[(L+R)/2];

        /*
        step_1 : pivot기준 좌, 우에 대소비교해서 넣기
         */
        do {
            // pivot보다 큰 것이 있으면 멈춘다
            while (data[left] < pivot) {
                left++;
            }
            // pivot보다 작은 값이 있으면 멈춘다
            while (data[right] > pivot) {
                right--;
            }

            // pivot 보다 큰데 왼쪽, 작은데 오른쪽에 있는 값을 서로 바꾼다
            if (left <= right) {
                int temp = data[left];
                data[left] = data[right];
                data[right] = temp;

                // 서로 교체 후, 아직 pivot에 이르기 전이라면 계속한다
                left++;
                right--;
            }

        } while (left <= right);

        /*
        step_2 : 재귀적으로 반복
         */
        if (L < right) {
            quickSort(data, L, right);
        }

        if (R > left) {
            quickSort(data, left, R);
        }

    }

}

