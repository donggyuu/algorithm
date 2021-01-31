public class QueueByLinkedList {

    public static void main(String[] args) {

        Queue<Integer> queue = new Queue<>();
        queue.insert(1);
        queue.insert(2);
        queue.insert(3);

        System.out.println(queue.peek()); // 1
        System.out.println(queue.remove()); // 1
        System.out.println(queue.peek()); // 2
    }

    /**
     * Node
     */
    static class Node<T> {
        private T data;
        private Node<T> next;

        public Node(T data) {
            this.data = data;
        }
    }

    /**
     * Queue
     */
    static class Queue<T> {

        private Node<T> front;
        private Node<T> rear;

        public boolean isEmpty() {
            return front == null;
        }

        public void insert(T data) {

            Node<T> newNode = new Node<>(data);
            newNode.next = null;

            if (isEmpty()) {
                front = newNode;
                rear = newNode;
            } else {
                rear.next = newNode;
                rear = newNode;
            }

        }

        public T peek() {

            if (isEmpty()) {
                // throw error
            }

            return front.data;
        }

        public T remove() {

            T data = peek();

            front = front.next;

            if (front == null) {
                rear = null;
            }

            return data;
        }

    }
}
