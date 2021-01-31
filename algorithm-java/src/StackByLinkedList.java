public class StackByLinkedList {

    public static void main(String[] args) {

        Stack<Integer> stack = new Stack<>();
        stack.push(1);
        stack.push(2);
        System.out.println(stack.peek()); // 2
        System.out.println(stack.pop()); // 2
        System.out.println(stack.peek()); // 1
        System.out.println(stack.pop()); // 1
        System.out.println(stack.isEmpty()); // true

    }

    static class Node<T> {
        private T data;
        private Node<T> next;

        public Node(T data) {
            this.data = data;
        }
    }

    static class Stack<T> {

        private Node<T> top;

        public void push(T data) {
            Node<T> node = new Node<>(data);
            node.next = top; // top은 기존의 node를 가리키고 있음
            top = node; // top을 추가된 node를 가리키도록 변경
        }

        public T pop() {
            if (top == null) {
                // throw "Stack is Empty"
            }

            T data = top.data;
            top = top.next;
            return data;
        }

        public T peek() {
            if (top == null) {
                // throw "Stack is Empty"
            }
            return top.data;
        }

        boolean isEmpty() {
            return top == null;
        }

    }


}
