public class SelectionSort {

    public static void main(String[] args) {

        // int[] intArray = new int[20];
        int data[] = {66, 11, 22, 44,  33};
        selectionSort(data);

        for (int i=0; i<data.length; i++) {
            System.out.print(data[i] + " ");
        }

    }

    // 전체에서 최소를 찾아서 하나씩 교체한다.

    public static void selectionSort(int[] data) {
        int size = data.length;
        int minIndex;
        int temp;

        // 마지막은 자동정렬이니, "i<size-1"로 해도 된다
        for (int i=0; i<size; i++) {
            minIndex = i;

            for (int j=i; j<size; j++ ) {
                if (data[minIndex] > data[j]) {
                    minIndex = j;
                }
            }

            // 가장 작은 것과 교환
            temp = data[minIndex];
            data[minIndex] = data[i];
            data[i] = temp;
        }
    }

}
