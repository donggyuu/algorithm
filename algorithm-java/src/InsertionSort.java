public class InsertionSort {

    public static void main(String[] args) {
        int[] data = {99,88,22,33,55};
        insertionSort(data);

        for (int datum : data) {
            System.out.print(datum + " ");
        }

    }

    public static void insertionSort(int[] data) {

        // i = 0 은 정렬된 상태로 가정
        // i = 1 번째의 데이터부터 비교
        for (int targetIndex = 1; targetIndex < data.length; targetIndex++) {
            int targetVal = data[targetIndex];

            // target-value와 그 왼쪽의 값을 비교해서 교체한다.
            for (int i=targetIndex-1; i>=0; i--) {

                if (data[i] > targetVal) {
                    // target-value가 더 작을 경우, i번째와 위치를 바꿈
                    data[i + 1] = data[i];
                    data[i] = targetVal;
                } else {
                    break;
                }

            }
        }

    }

}
