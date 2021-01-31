public class MergeSort {

    public static void main(String[] args) {

        int[] data = {99,88,22,33,55};
        mergeSort(data);

        for (int element : data) {
            System.out.println(element);
        }

    }

    public static void mergeSort(int[] data) {

        if (data.length < 2) {
            return;
        }

        /*
        배열을 2부분으로 나눈다
         */
        int mid = data.length / 2;
        int[] left = new int[mid];
        int[] right = new int[data.length - mid];

        // 사용 가능하도록 2개의 배열로 복사해서 나눔
        System.arraycopy(data, 0, left, 0, left.length);
        System.arraycopy(data, mid, right, 0, right.length);

        mergeSort(left);
        mergeSort(right);

        merge(data, left, right);
    }

    private static void merge(int[] dest, int[] left, int[] right) {

        int dIndex = 0;
        int lIndex = 0;
        int rIndex = 0;

        // left, right 모두 원소가 있는 상태에서 비교하여 합친다
        while (lIndex < left.length && rIndex < right.length) {
            if (left[lIndex] <= right[rIndex]) {
                dest[dIndex++] = left[lIndex++];
            } else {
                dest[dIndex++] = right[rIndex++];
            }
        }

        // 대소 비교 후, 남아있는 원소들을 합친다
        while (lIndex < left.length) {
            dest[dIndex++] = left[lIndex++];
        }

        while (rIndex < right.length) {
            dest[dIndex++] = right[rIndex++];
        }

    }

}
