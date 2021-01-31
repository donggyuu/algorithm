import java.util.ArrayList;

// TODO : 로직에 오류가 있어서 원하는 SysOut이 안나온다 -> 수정하기

public class MinHeap {

    public static void main(String[] args) {

        MinimumHeap heap = new MinimumHeap();
        heap.insert(3);
        heap.insert(4);
        heap.insert(5);
        heap.insert(7);
        heap.insert(10);
        // heap.delete();

        for (int i : heap.getHeap()) {
            if (i == 0) {
                continue;
            }

            System.out.println(i);
        }

    }

    static class MinimumHeap{
        private ArrayList<Integer> heap;

        public ArrayList<Integer> getHeap() {
            return heap;
        }

        public MinimumHeap() {
            heap = new ArrayList<>();
            heap.add(0); // 0은 default, heap의 삽입은 1인덱스부터(표기 쉽게하려고?)
        }

        /*
        삽입
        1. 배열의 제일 마지막에 새 노드 삽입
        2. 삽입한 새 노드 포함해서, 힙의 조건을 만족할 때까지 부모와 자식 노드를 교환 반복
         */
        public void insert(int data) {
            heap.add(data);
            int position = heap.size() - 1; // 배열의 제일 마지막에 삽입

            // 루트 노드까지 이동하지 않았고, 부모힙보다 자식힙이 더 크다면 -> 최소힙을 위해 노드 교환
            while (position > 1 && heap.get(position/2) < heap.get(position)) {

                // 부모와 자식 노드를 swap
                int temp = heap.get(position/2); // 부모 노드
                heap.set(position/2, heap.get(position)); // 부모노드 위치에 자식노드를 넣기
                heap.set(position, temp); // 자식노드에 부모노드를 넣기

                position /= 2; // 현재노드 위치를 재조정(부모노드로)
            }
        }

        /*
        삭제
        1. 루트노드 삭제
        2. 말단 노드를 루트노드 자리로 가져옴
        3. 자식노드와 비교하여 힙의 특성을 만족 -> 모든 노드가 힙 특성 만족까지 반복
         */
        public int delete() {

            int sizeHeap = heap.size() - 1;

            // heap 사이즈가 1보다 작다 = 값이 없으면 return 0
            if (sizeHeap < 1) {
                return 0;
            }

            // root-node 삭제(단말노드로 교체)
            int deleteData = heap.get(1);
            heap.set(1, heap.get(sizeHeap)); // 단말노드를 루트노드로
            heap.remove(sizeHeap); // 단말노드 삭제

            int position = 1;
            while ((position*2) < heap.size()) { // 자식노드가 heap사이즈보다 작을때가지

                /*
                좌,우 노드중 작은 노드와 교환해야 한다
                 */
                int min = heap.get(position*2); // 왼쪽자식노드를 일단 작은 노드로 설정
                int minPosition = position*2;

                // 오른쪽 자식노드가 더 작다면 그걸 최소 노드로
                if ((position*2+1) < heap.size() && min > heap.get(position*2+1)) {
                    min = heap.get(position*2+1);
                    minPosition = position*2+1;
                }

                /*
                현재 노드와 자식 노드를 비교한다
                 */
                if (heap.get(position) < min) {
                    break; // 최소힙 만족하면 종료
                }

                int temp = heap.get(position);
                heap.set(position, heap.get(minPosition));
                heap.set(minPosition, temp);
                position = minPosition;
            }

            return deleteData;
        }

    }
}
