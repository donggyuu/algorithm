public class BinarySearch {

    public static void main(String[] args) {

        int data[] = {1, 2, 3, 4, 5, 7, 10, 11, 13, 19}; // 정렬된 data
        binarySearch(10, data);
    }

    public static void binarySearch(int targetData, int[] data) {

        int mid;
        int left = 0;
        int right = data.length - 1;

        while (right >= left) {
            mid = (right + left) / 2;

            // 찾았다!
            if (targetData == data[mid]) {
                System.out.println("found target data, index : " + mid + ", data : "  + targetData);
                break;
            }

            // 못찾았으면 right, left를 update
            if (targetData < data[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

    }
}
