import java.io.IOException;

public class SinglyLinkedList {

    public static void main(String[] args) throws IOException {

        // TODO : 아래를 참고하여 SysOut까지 짜두기
        // https://freestrokes.tistory.com/84

    }


    /**
     * 하나의 노드 정의
     */
    class ListNode {

        /*
        data, link
         */
        private String data;
        public ListNode link;

        /*
        생성자
         */
        public ListNode() {
            this.data = null;
            this.link = null;
        }

        public ListNode(String data) {
            this.data = data;
            this.link = null;
        }

        public ListNode(String data, ListNode link) {
            this.data = data;
            this.link = link;
        }

        /*
        getter
         */
        public String getData() {
            return this.data;
        }
    }


    /**
     * 여러 노드로 구성된 연결리스트 정의
     */
    class LinkedList {

        private ListNode head;

        public LinkedList() {
            this.head = null;
        }

        /**
         *
         * preNode 다음에 newNode를 삽입(중간 삽입, 삽입 위치를 알 경우)
         */
        public void insertNode(ListNode preNode, String data) {

            ListNode newNode = new ListNode(data);

            /*
            상태 : preNode - newNode - otherNode
            노드의 연결상태를 수정
             */
            newNode.link = preNode.link;
            preNode.link = newNode;
        }


        /**
         * 제일 마지막에 newNode를 삽입(노드가 없거나 마지막에 삽입할 경우)
         */
        public void insertNode(String data) {

            ListNode newNode = new ListNode(data);

            if (head == null) {
                this.head = newNode;

            } else {
                ListNode tempNode = head;
                while(tempNode.link != null) {
                    tempNode = tempNode.link; // 다음 노드를 탐색
                }

                // 마지막 노드의 link가 newNode를 참조하도록
                tempNode.link = newNode;
            }
        }


        // TODO : 아래를 참고하여 삭제를 구현
        // https://freestrokes.tistory.com/84
        /**
         * preNode 다음의 Node를 삭제
         */
        public void deleteNode(String data) {

        }

        /**
         * 마지막 Node를 삭제
         */


        /**
         * 특정 data를 가진 node 검색
         */
        public ListNode searchNode(String data) {

            ListNode tempNode = this.head;

            while (tempNode != null) {
                if (data.equals(tempNode.getData())) {
                    return tempNode;
                } else {
                    tempNode = tempNode.link;
                }
            }

            return tempNode;
        }

    }


}
