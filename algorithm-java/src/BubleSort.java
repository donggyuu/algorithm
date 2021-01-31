public class BubleSort {

    public static void main(String[] args) {

        int data[] = {66, 10, 1, 34, 5, -10};

        bubleSort(data);

        // print
        for(int i=0; i<data.length; i++){
            System.out.print(data[i] + " ");
        }
    }

    public static void bubleSort(int[] data) {
        // 한 번 루프 돌 때마다, 마지막에 차례로 큰 수가 쌓인다
        for (int i=0; i < data.length; i++) { // 1.제일 오른쪽은 큰 수가 정렬되어 쌓인다
            for (int j=0; j<data.length-1 - i; j++) { // "1."이기 때문에, 정렬 안된 부분만 범위로
                if (data[j] > data[j+1]) {
                    int temp = data[j+1];
                    data[j+1] = data[j];
                    data[j] = temp;
                }
            }
        }
    }

}
